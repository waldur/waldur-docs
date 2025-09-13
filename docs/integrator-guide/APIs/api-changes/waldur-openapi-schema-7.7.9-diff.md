# OpenAPI schema diff - 7.7.9

## For version 7.7.9

### New Endpoints: None

-----------------------

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 95

--------------------------
GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_has_consent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_has_consent
              - Modified property: country
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/CountryEnum
                    - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_has_consent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/call-managing-organisations/

- Security changed
  - Deleted security requirements:

HEAD /api/call-managing-organisations/

- Security changed
  - Deleted security requirements:

GET /api/call-managing-organisations/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: country
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/CountryEnum
                    - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/CountryEnum
                - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/CountryEnum
                - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/CountryEnum
                - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/identity-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: client_secret
            - Properties changed
              - New property: attribute_mapping
              - New property: client_secret
              - New property: extra_fields
              - New property: user_claim
              - New property: user_field

POST /api/identity-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: client_secret
        - Properties changed
          - New property: attribute_mapping
          - New property: client_secret
          - New property: extra_fields
          - New property: user_claim
          - New property: user_field
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: client_secret
          - Properties changed
            - New property: attribute_mapping
            - New property: client_secret
            - New property: extra_fields
            - New property: user_claim
            - New property: user_field

GET /api/identity-providers/{provider}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: client_secret
          - Properties changed
            - New property: attribute_mapping
            - New property: client_secret
            - New property: extra_fields
            - New property: user_claim
            - New property: user_field

PATCH /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: attribute_mapping
          - New property: client_secret
          - New property: extra_fields
          - New property: user_claim
          - New property: user_field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: client_secret
          - Properties changed
            - New property: attribute_mapping
            - New property: client_secret
            - New property: extra_fields
            - New property: user_claim
            - New property: user_field

PUT /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: client_secret
        - Properties changed
          - New property: attribute_mapping
          - New property: client_secret
          - New property: extra_fields
          - New property: user_claim
          - New property: user_field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: client_secret
          - Properties changed
            - New property: attribute_mapping
            - New property: client_secret
            - New property: extra_fields
            - New property: user_claim
            - New property: user_field

GET /api/marketplace-categories/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-categories/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-categories/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-category-columns/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-category-columns/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-category-columns/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-category-groups/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-category-groups/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-category-groups/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true

POST /api/marketplace-course-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true

GET /api/marketplace-offering-referrals/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-offering-referrals/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-offering-referrals/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-offering-terms-of-service/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: has_user_consent
              - New required property: user_consent
            - Properties changed
              - New property: has_user_consent
              - New property: user_consent

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: has_user_consent
            - New required property: user_consent
          - Properties changed
            - New property: has_user_consent
            - New property: user_consent

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: has_user_consent
            - New required property: user_consent
          - Properties changed
            - New property: has_user_consent
            - New property: user_consent

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: has_user_consent
            - New required property: user_consent
          - Properties changed
            - New property: has_user_consent
            - New property: user_consent

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-plan-components/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-plan-components/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-plan-components/{id}/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-provider-offerings/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: country
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/CountryEnum
                    - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

HEAD /api/marketplace-provider-offerings/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/CountryEnum
                - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-offerings/groups/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

HEAD /api/marketplace-provider-offerings/groups/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/CountryEnum
                - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-public-offerings/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_has_consent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_has_consent
              - Modified property: country
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/CountryEnum
                    - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

HEAD /api/marketplace-public-offerings/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_has_consent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/RobotAccountStates
                - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

PATCH /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

PUT /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_has_consent
            - Modified property: country
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/CountryEnum
                  - New enum values: [AW AF AO AI AX AD AE AR AM AS AQ TF AG AU AZ BI BJ BQ BF BD BH BS BL BY BZ BM BO BR BB BN BT BV BW CF CA CC CL CN CI CM CD CG CK CO KM CV CR CU CW CX KY DJ DM DO DZ EC EG ER EH ET FJ FK FO FM GA GG GH GI GN GP GM GW GQ GD GL GT GF GU GY HK HM HN HT ID IM IN IO IR IQ IL JM JE JO JP KZ KE KG KH KI KN KR KW LA LB LR LY LC LI LK LS MO MF MA MD MG MV MX MH ML MM ME MN MP MZ MR MS MQ MU MW MY YT NA NC NE NF NG NI NU NP NR NZ OM PK PA PN PE PH PW PG PR KP PY PS PF QA RE RU RW SA SD SN SG GS SH SJ SB SL SV SM SO PM SS ST SR SZ SX SC SY TC TD TG TH TJ TK TM TL TO TT TN TR TV TW TZ UG UM UY US UZ VA VC VE VG VI VN VU WF WS YE ZA ZM ZW]

GET /api/marketplace-service-providers/

- Security changed
  - Deleted security requirements:

HEAD /api/marketplace-service-providers/

- Security changed
  - Deleted security requirements:

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: user_has_consent

GET /api/marketplace-service-providers/{uuid}/

- Security changed
  - Deleted security requirements:

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ENABLE_MOCK_COURSE_ACCOUNT_BACKEND

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ENABLE_MOCK_COURSE_ACCOUNT_BACKEND

POST /api/project-permissions-reviews/{uuid}/close/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: review_duration_in_days
                - Default changed from 7 to null

POST /api/proposal-protected-calls/{uuid}/rounds/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: review_duration_in_days
            - Default changed from 7 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: review_duration_in_days
              - Default changed from 7 to null

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: review_duration_in_days
              - Default changed from 7 to null

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: review_duration_in_days
            - Default changed from 7 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: review_duration_in_days
              - Default changed from 7 to null

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: review_duration_in_days
            - Default changed from 7 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: review_duration_in_days
              - Default changed from 7 to null

GET /api/support-issues/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: type
            - Properties changed
              - Modified property: type
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/IssueTypeEnum
                - Default changed from 'Informational' to null

POST /api/support-issues/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: type
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Schemas deleted: #/components/schemas/IssueTypeEnum
            - Default changed from 'Informational' to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: type
          - Properties changed
            - Modified property: type
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/IssueTypeEnum
              - Default changed from 'Informational' to null

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: type
          - Properties changed
            - Modified property: type
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/IssueTypeEnum
              - Default changed from 'Informational' to null

PATCH /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: type
          - Properties changed
            - Modified property: type
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/IssueTypeEnum
              - Default changed from 'Informational' to null

PUT /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: type
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Schemas deleted: #/components/schemas/IssueTypeEnum
            - Default changed from 'Informational' to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: type
          - Properties changed
            - Modified property: type
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/IssueTypeEnum
              - Default changed from 'Informational' to null

POST /api/support-issues/{uuid}/sync/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: type
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Schemas deleted: #/components/schemas/IssueTypeEnum
            - Default changed from 'Informational' to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: type
          - Properties changed
            - Modified property: type
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/IssueTypeEnum
              - Default changed from 'Informational' to null

GET /api/support-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: issue_type
                - Type changed from 'string' to ''
                - Deleted enum values: [Informational Service Request Change Request Incident]

POST /api/support-templates/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: issue_type
            - Type changed from 'string' to ''
            - Deleted enum values: [Informational Service Request Change Request Incident]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: issue_type
              - Type changed from 'string' to ''
              - Deleted enum values: [Informational Service Request Change Request Incident]

GET /api/support-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: issue_type
              - Type changed from 'string' to ''
              - Deleted enum values: [Informational Service Request Change Request Incident]

PATCH /api/support-templates/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: issue_type
            - Type changed from 'string' to ''
            - Deleted enum values: [Informational Service Request Change Request Incident]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: issue_type
              - Type changed from 'string' to ''
              - Deleted enum values: [Informational Service Request Change Request Incident]

PUT /api/support-templates/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: issue_type
            - Type changed from 'string' to ''
            - Deleted enum values: [Informational Service Request Change Request Incident]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: issue_type
              - Type changed from 'string' to ''
              - Deleted enum values: [Informational Service Request Change Request Incident]
