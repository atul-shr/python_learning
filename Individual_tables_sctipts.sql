drop table [dbo].[agreements];

CREATE TABLE [dbo].[agreements](
agreement_id varchar(500),
	usageCd	varchar(500),
relationshipId	varchar(500),
account_bookOfBusinessCd	varchar(500),
account_borKeyVal	varchar(500),
account_accountId	varchar(500),
account_statusCd	varchar(500),
account_accountTypeCd	varchar(500),
account_lobCd	varchar(500),
account_securityCommunicationCd	varchar(500),
account_securityPrivacyInd	varchar(500),
account_accountNum	varchar(500),
account_currencyCd	varchar(500),
account_optionsTradingInd	varchar(500),
account_newClientIdReservedInd	varchar(500),
account_newClientId	varchar(500),
account_accMinorClsCd varchar(1000));

drop table [dbo].[streetAddresses];
CREATE TABLE [dbo].[streetAddresses](
streetAddresses_id varchar(500),
uniqueId		varchar(1000),
relationshipId		varchar(1000),
usageCd		varchar(1000),
address_addressId		varchar(1000),
address_startDttm		varchar(1000),
address_endDttm		varchar(1000),
address_unitNum		varchar(1000),
address_unitTypeCd		varchar(1000),
address_streetNum		varchar(1000),
address_streetName		varchar(1000),
address_streetOrientationTxt		varchar(1000),
address_streetTypeCd		varchar(1000),
address_streetDirectionCd		varchar(1000),
address_streetSuffixCd		varchar(1000),
address_cityName		varchar(1000),
address_postalCode		varchar(1000),
address_territoryCd		varchar(1000),
address_countryCd		varchar(1000),
address_ruralRouteNum		varchar(1000),
address_ruralRouteTypeCd		varchar(1000),
address_poBox		varchar(1000),
address_postalStationTxt		varchar(1000),
lastUpdate_userId		varchar(1000),
lastUpdate_userTypeCd		varchar(1000),
lastUpdate_asOfDttm		varchar(1000),
lastUpdate_hash		varchar(1000)
);



drop table [dbo].emailAddresses;
CREATE TABLE [dbo].emailAddresses(
emailAddresses_id varchar(1000),
uniqueId	varchar(1000),
relationshipId	varchar(1000),
usageCd	varchar(1000),
emailTxt	varchar(1000),
email_startDttm	varchar(1000),
email_endDttm	varchar(1000),
lastUpdate_userId	varchar(1000),
lastUpdate_userTypeCd	varchar(1000),
lastUpdate_asOfDttm	varchar(1000),
lastUpdate_hash	varchar(1000)
);

drop table dbo.telephoneAddresses	;
create table dbo.telephoneAddresses	
(	
telephoneAddresses_id varchar(1000),
uniqueId	varchar(1000),
relationshipId	varchar(1000),
usageCd	varchar(1000),
telephone_startDttm	varchar(1000),
telephone_endDttm	varchar(1000),
telephone_localNum	varchar(1000),
telephone_countryCodeNum	varchar(1000),
telephone_areaCodeNum	varchar(1000),
telephone_extensionNum	varchar(1000),
lastUpdate_userId	varchar(1000),
lastUpdate_userTypeCd	varchar(1000),
lastUpdate_asOfDttm	varchar(1000),
lastUpdate_hash	varchar(1000)
);

drop table dbo.identifications	;
create table dbo.identifications	
(	
identifications_id varchar(1000),
uniqueId	varchar(1000),
identificationId	varchar(1000),
typeCd	varchar(1000),
identificationNum	varchar(1000),
statusCd	varchar(1000),
startDt	varchar(1000),
endDt	varchar(1000),
issuingTerritoryCd	varchar(1000),
issuingCountryCd	varchar(1000),
documentFormatTypeCd	varchar(1000),
documentLocationTxt	varchar(1000),
lastUpdate_userId	varchar(1000),
lastUpdate_userTypeCd	varchar(1000),
lastUpdate_asOfDttm	varchar(1000),
lastUpdate_hash	varchar(1000),
signedDt	varchar(1000),
requestedDt	varchar(1000),
reviewedDt	varchar(1000),
reviewerId	varchar(1000),
retentionNum	varchar(1000),
issuingPartyFullName	varchar(1000),
documentName	varchar(1000)
);

drop table dbo.alternateKeys	;
create table dbo.alternateKeys	
(	
alternateKeys_id varchar(1000),
alternateKey	varchar(1000),
keyTypeCd	varchar(1000));

drop table dbo.kyc;

create table dbo.kyc	
(	
kyc_id varchar(1000),
uniqueId	varchar(1000),
startDttm	varchar(1000),
endDttm	varchar(1000),
annualIncomeAmt	varchar(1000),
estimateNetWorthAmt	varchar(1000),
shareholderNum	varchar(1000),
dependentsNum	varchar(1000),
investmentKnowledgeCd	varchar(1000),
yearsStockInvestmentExperienceCnt	varchar(1000),
yearsMutualFundInvestmentExperienceCnt	varchar(1000),
yearsBondInvestmentExperienceCnt	varchar(1000),
yearsOptionsInvestmentExperienceCnt	varchar(1000),
yearsShortSellingInvestmentExperienceCnt	varchar(1000),
lastUpdate_userId	varchar(1000),
lastUpdate_userTypeCd	varchar(1000),
lastUpdate_asOfDttm	varchar(1000),
lastUpdate_hash	varchar(1000),
proTypeCd	varchar(1000)
);

drop table dbo.fatca;
create table dbo.fatca	
(	
fatca_id varchar(1000),
startDttm	varchar(1000),
endDttm	varchar(1000),
statusCd	varchar(1000),
statusDt	varchar(1000),
classificationTypeCd	varchar(1000),
usTaxRecipientTypeCd	varchar(1000),
qualifiedInvestorInd	varchar(1000),
usSelfDeclaredInd	varchar(1000),
usIndiciaInd	varchar(1000),
usIndiciaEffectiveDt	varchar(1000),
lastUpdate	varchar(1000),
usBornInd	varchar(1000)
);

drop table dbo.crs		;
create table dbo.crs		
(	
crs_id varchar(1000),
uniqueId	varchar(1000),
startDttm	varchar(1000),
endDttm	varchar(1000),
statusCd	varchar(1000),
statusDt	varchar(1000),
classificationTypeCd	varchar(1000),
certificationDt	varchar(1000),
attestationDt	varchar(1000),
certificationSignedInd	varchar(1000),
preexistingAgreementInd	varchar(1000),
lastUpdate	varchar(1000),
usCitizenInd	varchar(1000),
certifications_tinRequiredInd	varchar(1000),
certifications_tinOnFileInd	varchar(1000),
certifications_certificationId	varchar(1000),
certifications_lastUpdate	varchar(1000),
certifications_documentNum	varchar(1000),
certifications_countryCd	varchar(1000),
certifications_documentTypeCd	varchar(1000)
);

drop table dbo.individuals	;
create table dbo.individuals	
(	
individuals_id varchar(1000),
uniqueId	varchar(1000),
partyId	varchar(1000),
startDttm	varchar(1000),
endDttm	varchar(1000),
partyTypeCd	varchar(1000),
proTypeCd	varchar(1000),
statusCd	varchar(1000),
globalIdentificationNum	varchar(1000),
bankruptcyDt	varchar(1000),
correspondenceTypeCd	varchar(1000),
correspondenceLangCd	varchar(1000),
nonResidentCds_nonResidentStatusCd	varchar(1000),
nonResidentCds_accountNumber	varchar(1000),
names_nameId	varchar(1000),
names_nameTypeCd	varchar(1000),
names_givenName	varchar(1000),
names_middleName	varchar(1000),
names_familyName	varchar(1000),
names_titleTypeCd	varchar(1000),
names_suffixTypeCd	varchar(1000),
names_startDttm	varchar(1000),
names_endDttm	varchar(1000),
names_lastUpdate_userId	varchar(1000),
names_lastUpdate_userTypeCd	varchar(1000),
names_lastUpdate_asOfDttm	varchar(1000),
names_lastUpdate_hash	varchar(1000),
residenceCountryCd	varchar(1000),
genderTypeCd	varchar(1000),
maritalStatusCd	varchar(1000),
birthDt	varchar(1000),
deceasedDt	varchar(1000),
birthCountryCd	varchar(1000),
nonResidentStatusCd	varchar(1000),
citizenships_citizenshipId	varchar(1000),
citizenships_startDttm	varchar(1000),
citizenships_endDttm	varchar(1000),
citizenships_citizenshipCd	varchar(1000),
citizenships_lastUpdate_userId	varchar(1000),
citizenships_lastUpdate_userTypeCd	varchar(1000),
citizenships_lastUpdate_asOfDttm	varchar(1000),
citizenships_lastUpdate_hash	varchar(1000),
lastUpdate_userId	varchar(1000),
lastUpdate_userTypeCd	varchar(1000),
lastUpdate_asOfDttm	varchar(1000),
lastUpdate_hash	varchar(1000),
partyProfile_partyId	varchar(1000),
relationshipTypeCd	varchar(1000),
employment_statusCd	varchar(1000),
employment_employerName	varchar(1000),
employment_occupationTypeCd	varchar(1000),
employment_socInfo	varchar(1000),
employment_jobTitleTxt	varchar(1000),
employment_streetAddress_usageCd	varchar(1000),
employment_streetAddress_relationshipId	varchar(1000),
employment_streetAddress_address_streetNumSuffixVal	varchar(1000),
employment_streetAddress_address_territoryCd	varchar(1000),
employment_streetAddress_address_ruralRouteNum	varchar(1000),
employment_streetAddress_address_ruralRouteTypeCd	varchar(1000),
employment_streetAddress_address_cityName	varchar(1000),
employment_streetAddress_address_unitTypeCd	varchar(1000),
employment_streetAddress_address_streetTypeCd	varchar(1000),
employment_streetAddress_address_streetName	varchar(1000),
employment_streetAddress_address_endDttm	varchar(1000),
employment_streetAddress_address_streetDirectionCd	varchar(1000),
employment_streetAddress_address_addressId	varchar(1000),
employment_streetAddress_address_addressLine	varchar(1000),
employment_streetAddress_address_unitNum	varchar(1000),
employment_streetAddress_address_postalCode	varchar(1000),
employment_streetAddress_address_startDttm	varchar(1000),
employment_streetAddress_address_poBox	varchar(1000),
employment_streetAddress_address_countryCd	varchar(1000),
employment_streetAddress_address_postalStationTxt	varchar(1000),
employment_streetAddress_address_streetNum	varchar(1000),
employment_streetAddress_lastUpdate	varchar(1000),
employment_telephone_startDttm	varchar(1000),
employment_telephone_endDttm	varchar(1000),
employment_telephone_localNum	varchar(1000),
employment_telephone_countryCodeNum	varchar(1000),
employment_telephone_areaCodeNum	varchar(1000),
employment_telephone_extensionNum	varchar(1000)
);

drop table dbo.misc	;

create table dbo.misc	
(	
misc_id varchar(1000),
referringAgent_acf2id	varchar(1000),
referringAgent_transitNumber	varchar(1000),
applicationType	varchar(1000),
beaconScore	varchar(1000)
);

drop table dbo.interestedAccounts	;
create table dbo.interestedAccounts	
(	
interestedAccounts_id varchar(1000),
relationshipToAccount	varchar(1000),
accountNumber	varchar(1000),
allocationPercentage	varchar(1000),
uniqueId	varchar(1000)
);

drop table dbo.additionals;
create table dbo.additionals	
(	
additionals_id varchar(1000),
usageCd	varchar(1000),
ownershipPercent	varchar(1000),
actionType	varchar(1000),
cmMasterClientId	varchar(1000),
appId	varchar(1000));
