import json
import pyodbc
from datetime import datetime


# create raw data
def create_raw(conn, ls):
    print("Create")
    cnt = 0
    cur = conn.cursor()
    cur.execute("delete from dbo.json_flatten_raw;")
    for rec in ls:
        cnt += 1
        cur.execute("insert into dbo.json_flatten_raw(item_no,item_name,item_value) values (?,?,?);",
                    (cnt, bytes(str(rec[0]), 'utf-8'), bytes(str(rec[1]), 'utf-8'))
                    )
    conn.commit()


# creation of leaf records
def break_down_leaf(conn,now):
    print("Create Child Records")
    cnt = 0
    split_leaf_list = []
    split_leaf = []
    cur_read = conn.cursor()
    #  cur_ins = conn1.cursor()
    cur_read.execute("select item_no , item_name , item_value  from dbo.json_flatten_raw;")
    for row in cur_read:
        split_leaf_list.append(row)

    for inner_row in split_leaf_list:
        #  print(row[0],row[1],row[2])
        split_leaf = inner_row[1].split(".")
        #  print(split_leaf)
        for child_rec in split_leaf:
            cnt += 1
            cur_read.execute(
                "insert into dbo.json_flatten(item_no,item_name,parent_item_no,insert_date) values (?,?,?,?);",
                (cnt, child_rec, inner_row[0], now)
            )
        cnt = 0
    conn.commit()


# read json file into records
def flattenDict(d, result=None, index=None, Key=None):
    if result is None:
        result = {}
    if isinstance(d, (list, tuple)):
        for indexB, element in enumerate(d):
            if Key is not None:
                newkey = Key
            flattenDict(element, result, index=indexB, Key=newkey)
    elif isinstance(d, dict):
        for key in d:
            value = d[key]
            if Key is not None and index is not None:
                newkey = ".".join([Key, (str(key).replace(" ", "") + str(index))])
            elif Key is not None:
                newkey = ".".join([Key, (str(key).replace(" ", ""))])
            else:
                newkey = str(key).replace(" ", "")
            flattenDict(value, result, index=None, Key=newkey)
    else:
        result[Key] = d
    return result


def convert_data_to_list(ls):
    # cur = conn.cursor()
    # cur.execute("delete from dbo.agreements;")
    all_list = []
    for all_rec in ls:
        if "." in all_rec[0]:
            rec_split = str(all_rec[0]).split(".")
            rec_split.append(all_rec[1])
        else:
            rec_split = list(all_rec)
        # print(rec_split)
        all_list.append(rec_split)
    return all_list


def process_agreements_data(l, c):
    tab_nm = ''
    tab_row_data = []
    len_idx = 0
    row_ind = 0
    row_seq = 0
    agg_items = ['?' for item in range(1, 18)]
    # print(agg_items)
    agg_str_qry = """ insert into agreements(agreement_id
                                          ,usageCd
                                          ,relationshipId
                                          ,account_bookOfBusinessCd
                                          ,account_borKeyVal
                                          ,account_accountId
                                          ,account_statusCd
                                          ,account_accountTypeCd
                                          ,account_lobCd
                                          ,account_securityCommunicationCd
                                          ,account_securityPrivacyInd
                                          ,account_accountNum
                                          ,account_currencyCd
                                          ,account_optionsTradingInd
                                          ,account_newClientIdReservedInd
                                          ,account_newClientId
                                          ,account_accMinorClsCd)
                                    values (%s);""" % ','.join(agg_items)
    cur = c.cursor()
    # print(agg_str_qry)
    c.execute("delete from dbo.agreements")
    for tables_rec in l:
        if tables_rec[0] == "agreements":
            len_idx = len(tables_rec) - 1
            try:
                calc_row_id = tables_rec[1][-1:]
            except:
                calc_row_id = 0
            # print(tables_rec)
            if tab_nm == tables_rec[0] and calc_row_id == row_ind:  # and tab_row == tables_rec[0]:
                tab_row_data.append(tables_rec[len_idx])
            else:

                tab_row_data.insert(0, row_seq)
                # print(tab_nm + str(tab_row_data))
                if len(tab_row_data) != 17:
                    tab_row_data.append(None)
                if tab_row_data == [0, None]:
                    pass
                else:
                    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
                              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
                              tab_row_data[9], tab_row_data[10], tab_row_data[11], tab_row_data[12], tab_row_data[13],
                              tab_row_data[14], tab_row_data[15], tab_row_data[16]
                              )
                if tab_nm != tables_rec[0]:
                    row_seq = 0
                row_seq += 1
                tab_row_data = []
                tab_row_data.append(tables_rec[len_idx])
            tab_nm = tables_rec[0]
            row_ind = calc_row_id
    # print(tab_nm + str(tab_row_data))
    tab_row_data.insert(0, row_seq)
    if len(tab_row_data) != 17:
        tab_row_data.append(None)

    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
              tab_row_data[9], tab_row_data[10], tab_row_data[11], tab_row_data[12], tab_row_data[13],
              tab_row_data[14], tab_row_data[15], tab_row_data[16]
              )
    c.commit()
    # print(tab_nm + '--' + tab_row + '--' + str(tab_data))


def process_email_data(l, c):
    tab_nm = ''
    tab_row_data = []
    len_idx = 0
    row_ind = 0
    row_seq = 0
    agg_items = ['?' for item in range(1, 12)]
    # print(agg_items)
    agg_str_qry = """ insert into emailAddresses(emailAddresses_id
                                                ,uniqueId
                                                ,relationshipId
                                                ,usageCd
                                                ,emailTxt
                                                ,email_startDttm
                                                ,email_endDttm
                                                ,lastUpdate_userId
                                                ,lastUpdate_userTypeCd
                                                ,lastUpdate_asOfDttm
                                                ,lastUpdate_hash)
                                    values (%s);""" % ','.join(agg_items)
    cur = c.cursor()
    # print(agg_str_qry)
    c.execute("delete from dbo.emailAddresses")
    for tables_rec in l:
        if tables_rec[0] == "emailAddresses":
            # print(tables_rec)
            len_idx = len(tables_rec) - 1
            try:
                calc_row_id = tables_rec[1][-1:]
            except:
                calc_row_id = 0
            # print(tables_rec)
            if tab_nm == tables_rec[0] and calc_row_id == row_ind:  # and tab_row == tables_rec[0]:
                tab_row_data.append(tables_rec[len_idx])
            else:

                tab_row_data.insert(0, row_seq)
                # print(tab_nm + str(tab_row_data))
                if len(tab_row_data) != 11:
                    tab_row_data.append(None)
                if tab_row_data == [0, None]:
                    pass
                else:
                    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
                              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
                              tab_row_data[9], tab_row_data[10]
                              )
                    pass
                if tab_nm != tables_rec[0]:
                    row_seq = 0
                row_seq += 1
                tab_row_data = []
                tab_row_data.append(tables_rec[len_idx])
            tab_nm = tables_rec[0]
            row_ind = calc_row_id
    # print(tab_nm + str(tab_row_data))
    tab_row_data.insert(0, row_seq)
    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
              tab_row_data[9], tab_row_data[10]
              )
    c.commit()


def process_tel_add_data(l, c):
    tab_nm = ''
    tab_row_data = []
    len_idx = 0
    row_ind = 0
    row_seq = 0
    agg_items = ['?' for item in range(1, 15)]
    # print(agg_items)
    agg_str_qry = """ insert into telephoneAddresses(telephoneAddresses_id
                                                ,uniqueId
                                                ,relationshipId
                                                ,usageCd
                                                ,telephone_startDttm
                                                ,telephone_endDttm
                                                ,telephone_localNum
                                                ,telephone_countryCodeNum
                                                ,telephone_areaCodeNum
                                                ,telephone_extensionNum
                                                ,lastUpdate_userId
                                                ,lastUpdate_userTypeCd
                                                ,lastUpdate_asOfDttm
                                                ,lastUpdate_hash
                                                )
                                    values (%s);""" % ','.join(agg_items)
    cur = c.cursor()
    # print(agg_str_qry)
    c.execute("delete from dbo.telephoneAddresses")
    for tables_rec in l:
        if tables_rec[0] == "telephoneAddresses":
            # print(tables_rec)
            len_idx = len(tables_rec) - 1
            try:
                calc_row_id = tables_rec[1][-1:]
            except:
                calc_row_id = 0
            # print(tables_rec)
            if tab_nm == tables_rec[0] and calc_row_id == row_ind:  # and tab_row == tables_rec[0]:
                tab_row_data.append(tables_rec[len_idx])
            else:

                tab_row_data.insert(0, row_seq)
                # print(tab_nm + str(tab_row_data))
                if len(tab_row_data) != 14:
                    tab_row_data.append(None)
                if tab_row_data == [0, None]:
                    pass
                else:
                    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
                              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
                              tab_row_data[9], tab_row_data[10], tab_row_data[11], tab_row_data[12], tab_row_data[13]
                              )
                    pass
                if tab_nm != tables_rec[0]:
                    row_seq = 0
                row_seq += 1
                tab_row_data = []
                tab_row_data.append(tables_rec[len_idx])

            # if 'emailAddresses' != tables_rec[0]:
            #     break
            tab_nm = tables_rec[0]
            row_ind = calc_row_id
    tab_row_data.insert(0, row_seq)
    # print(tab_nm + str(tab_row_data))
    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
              tab_row_data[9], tab_row_data[10], tab_row_data[11], tab_row_data[12], tab_row_data[13]
              )
    c.commit()


def process_identifications_data(l, c):
    tab_nm = ''
    tab_row_data = []
    len_idx = 0
    row_ind = 0
    row_seq = 0
    agg_items = ['?' for item in range(1, 24)]
    # print(agg_items)
    agg_str_qry = """ insert into identifications(identifications_id
                                                    ,uniqueId
                                                    ,identificationId
                                                    ,typeCd
                                                    ,identificationNum
                                                    ,statusCd
                                                    ,startDt
                                                    ,endDt
                                                    ,issuingTerritoryCd
                                                    ,issuingCountryCd
                                                    ,documentFormatTypeCd
                                                    ,documentLocationTxt
                                                    ,lastUpdate_userId
                                                    ,lastUpdate_userTypeCd
                                                    ,lastUpdate_asOfDttm
                                                    ,lastUpdate_hash
                                                    ,signedDt
                                                    ,requestedDt
                                                    ,reviewedDt
                                                    ,reviewerId
                                                    ,retentionNum
                                                    ,issuingPartyFullName
                                                    ,documentName
                                                )
                                    values (%s);""" % ','.join(agg_items)
    cur = c.cursor()
    # print(agg_str_qry)
    c.execute("delete from dbo.identifications")
    for tables_rec in l:
        if tables_rec[0] == "identifications":
            # print(tables_rec)
            len_idx = len(tables_rec) - 1
            try:
                calc_row_id = tables_rec[1][-1:]
            except:
                calc_row_id = 0
            # print(tables_rec)
            if tab_nm == tables_rec[0] and calc_row_id == row_ind:  # and tab_row == tables_rec[0]:
                tab_row_data.append(tables_rec[len_idx])
            else:

                tab_row_data.insert(0, row_seq)
                # print(tab_nm + str(tab_row_data))
                if len(tab_row_data) != 24:
                    tab_row_data.append(None)
                if tab_row_data == [0, None]:
                    pass
                else:
                    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
                              tab_row_data[4], tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8],
                              tab_row_data[9], tab_row_data[10], tab_row_data[11], tab_row_data[12], tab_row_data[13],
                              tab_row_data[14], tab_row_data[15], tab_row_data[16], tab_row_data[17], tab_row_data[18],
                              tab_row_data[19], tab_row_data[20], tab_row_data[21], tab_row_data[22]
                              )
                    pass
                if tab_nm != tables_rec[0]:
                    row_seq = 0
                row_seq += 1
                tab_row_data = []
                tab_row_data.append(tables_rec[len_idx])

            # if 'emailAddresses' != tables_rec[0]:
            #     break
            tab_nm = tables_rec[0]
            row_ind = calc_row_id
    tab_row_data.insert(0, row_seq)
    # print(tab_nm + str(tab_row_data))

    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3], tab_row_data[4],
              tab_row_data[5], tab_row_data[6], tab_row_data[7], tab_row_data[8], tab_row_data[9], tab_row_data[10],
              tab_row_data[11], tab_row_data[12], tab_row_data[13], tab_row_data[14], tab_row_data[15],
              tab_row_data[16], tab_row_data[17], tab_row_data[18], tab_row_data[19], tab_row_data[20],
              tab_row_data[21], tab_row_data[22]
              )
    c.commit()


def process_interestedAccounts_data(l, c):
    tab_nm = ''
    tab_row_data = []
    len_idx = 0
    row_ind = 0
    row_seq = 0
    agg_items = ['?' for item in range(1, 6)]
    # print(agg_items)
    agg_str_qry = """ insert into interestedAccounts(interestedAccounts_id
                                                ,relationshipToAccount
                                                ,accountNumber
                                                ,allocationPercentage
                                                ,uniqueId
                                                )
                                    values (%s);""" % ','.join(agg_items)
    cur = c.cursor()
    # print(agg_str_qry)
    c.execute("delete from dbo.interestedAccounts")
    for tables_rec in l:
        if tables_rec[0] == "interestedAccounts":
            # print(tables_rec)
            len_idx = len(tables_rec) - 1
            try:
                calc_row_id = tables_rec[1][-1:]
            except:
                calc_row_id = 0
            # print(tables_rec)
            if tab_nm == tables_rec[0] and calc_row_id == row_ind:  # and tab_row == tables_rec[0]:
                tab_row_data.append(tables_rec[len_idx])
            else:

                tab_row_data.insert(0, row_seq)
                # print(tab_nm + str(tab_row_data))
                if len(tab_row_data) != 5:
                    tab_row_data.append(None)
                if tab_row_data == [0, None]:
                    pass
                else:
                    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3],
                              tab_row_data[4]
                              )
                    pass
                if tab_nm != tables_rec[0]:
                    row_seq = 0
                row_seq += 1
                tab_row_data = []
                tab_row_data.append(tables_rec[len_idx])

            # if 'emailAddresses' != tables_rec[0]:
            #     break
            tab_nm = tables_rec[0]
            row_ind = calc_row_id
    tab_row_data.insert(0, row_seq)
    # print(tab_nm + str(tab_row_data))

    c.execute(agg_str_qry, tab_row_data[0], tab_row_data[1], tab_row_data[2], tab_row_data[3], tab_row_data[4]
              )
    c.commit()


def main():
    #  datetime object containing current date and time
    now = datetime.now()

    # connection creation to SQL Server
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=LAPTOP-21RC5VEQ;"
        "Database=json;"
        "Trusted_Connection=yes;"
    )

    # read json source file
    with open("source.json", "r") as rj:
        response = rj.read()
    res = json.loads(response)
    raw_list = []

    # create list of records from json
    for i in flattenDict(res).items():
        # print(i)
        raw_list.append(i)

    full_data = convert_data_to_list(raw_list)

    # call function of raw rec creation
    create_raw(conn,raw_list)

    # call function of child rec creation
    break_down_leaf(conn,now)

    process_agreements_data(full_data, conn)

    process_email_data(full_data, conn)

    process_tel_add_data(full_data, conn)

    process_identifications_data(full_data, conn)

    process_interestedAccounts_data(full_data, conn)

    conn.close()


if __name__ == '__main__':
    main()

