# eduGAIN

## Overview

[eduGAIN](https://wiki.geant.org/display/eduGAIN/eduGAIN+Home) is a global federation of identity and service
providers, based technically on SAML2.

In order to allow eduGAIN users to access Waldur, there are two steps:

- Waldur deployment must be registered as a service provider in eduGAIN federation.
- Waldur must get a list of identities that are trusted for authentication.

!!! tip
    SAML is a complicated and fragile technology. GEANT provides an alternative to direct integration of SAML -
    [eduTEAMS](eduTEAMS.md), which exposes an OpenID Connect protocol for service providers.

Waldur relies on [djangosaml2](https://djangosaml2.readthedocs.io/) for the heavylifting of SAML processing,
so for fine tuning configuration, contact corresponding project documentation.

## Registering Waldur as Service Provider

### Add SAML configuration to Waldur Mastermind configuration

Example configuration is below, please adjust to your specific deployment. Once applied, service metadata will be
visible at Waldur deployment URL: ``https://waldur.example.com/api-auth/saml2/metadata/``. That data needs to be
propagated to the federation operator for inclusion into the federation.

!!! tip
    [Managed ansible](../managing-with-ansible.md) simplifies configuration of the eduGAIN integration and should
    be a preferred method for all supported deployments.

```python
import datetime

import saml2
from saml2.entity_category.edugain import COC


WALDUR_AUTH_SAML2 = {
    # used for assigning the registration method to the user
    'name': 'saml2',
    # full path to the xmlsec1 binary program
    'xmlsec_binary': '/usr/bin/xmlsec1',
    # required for assertion consumer, single logout services and entity ID
    'base_url': '',
    # directory with attribute mapping
    'attribute_map_dir': '',
    # set to True to output debugging information
    'debug': False,
    # IdPs metadata XML files stored locally
    'idp_metadata_local': [],
    # IdPs metadata XML files stored remotely
    'idp_metadata_remote': [],
    # logging
    # empty to disable logging SAML2-related stuff to file
    'log_file': '',
    'log_level': 'INFO',
    # Indicates if the entity will sign the logout requests
    'logout_requests_signed': 'true',
    # Indicates if the authentication requests sent should be signed by default
    'authn_requests_signed': 'true',
    # Identifies the Signature algorithm URL according to the XML Signature specification
    # SHA1 is used by default
    'signature_algorithm': None,
    # Identifies the Message Digest algorithm URL according to the XML Signature specification
    # SHA1 is used by default
    'digest_algorithm': None,
    # Identified NameID format to use. None means default, empty string ("") disables addition of entity
    'nameid_format': None,
    # PEM formatted certificate chain file
    'cert_file': '',
    # PEM formatted certificate key file
    'key_file': '',
    # SAML attributes that are required to identify a user
    'required_attributes': [],
    # SAML attributes that may be useful to have but not required
    'optional_attributes': [],
    # mapping between SAML attributes and User fields
    'saml_attribute_mapping': {},
    # organization responsible for the service
    # you can set multilanguage information here
    'organization': {},
    # links to the entity categories
    'categories': [COC],
    # attributes required by CoC
    # https://wiki.refeds.org/display/CODE/SAML+2+Profile+for+the+Data+Protection+Code+of+Conduct
    'privacy_statement_url': 'http://example.com/privacy-policy/',
    'display_name': 'Service provider display name',
    'description': 'Service provider description',
    # mdpi attributes
    'registration_policy': 'http://example.com/registration-policy/',
    'registration_authority': 'http://example.com/registration-authority/',
    'registration_instant': datetime.datetime(2017, 1, 1).isoformat(),
    'ENABLE_SINGLE_LOGOUT': False,
    'ALLOW_TO_SELECT_IDENTITY_PROVIDER': True,
    'IDENTITY_PROVIDER_URL': None,
    'IDENTITY_PROVIDER_LABEL': None,
    'DEFAULT_BINDING': saml2.BINDING_HTTP_POST,
    'DISCOVERY_SERVICE_URL': None,
    'DISCOVERY_SERVICE_LABEL': None,
}
```

### Example of generated metadata

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ns0:EntityDescriptor xmlns:ns0="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:ns1="urn:oasis:names:tc:SAML:metadata:attribute" xmlns:ns2="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:ns4="urn:oasis:names:tc:SAML:metadata:algsupport" xmlns:ns5="urn:oasis:names:tc:SAML:metadata:rpi" xmlns:ns6="urn:oasis:names:tc:SAML:metadata:ui" xmlns:ns7="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" entityID="https://api.etais.ee/api-auth/saml2/metadata/">
   <ns0:Extensions>
      <ns1:EntityAttributes>
         <ns2:Attribute Name="http://macedir.org/entity-category" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
            <ns2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xsi:type="xs:string">http://www.geant.net/uri/dataprotection-code-of-conduct/v1</ns2:AttributeValue>
         </ns2:Attribute>
      </ns1:EntityAttributes>
      <ns4:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
      <ns4:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#sha224" />
      <ns4:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
      <ns4:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#sha384" />
      <ns4:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2000/09/xmldsig#dsa-sha1" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2009/xmldsig11#dsa-sha256" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha224" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha224" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha384" />
      <ns4:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512" />
      <ns5:RegistrationInfo registrationAuthority="http://taat.edu.ee" registrationInstant="2017-01-01T00:00:00">
         <ns5:RegistrationPolicy xml:lang="en">http://taat.edu.ee/main/wp-content/uploads/Federation_Policy_1.3.pdf</ns5:RegistrationPolicy>
      </ns5:RegistrationInfo>
   </ns0:Extensions>
   <ns0:SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" AuthnRequestsSigned="true" WantAssertionsSigned="true">
      <ns0:Extensions>
         <ns6:UIInfo>
            <ns6:DisplayName xml:lang="en">ETAIS Self-Service</ns6:DisplayName>
            <ns6:Description xml:lang="en">Self-service for users of Estonian Scientific Computing Infrastructure (ETAIS)</ns6:Description>
            <ns6:Logo>https://minu.etais.ee/login-logo.png</ns6:Logo>
            <ns6:PrivacyStatementURL xml:lang="en">https://minu.etais.ee/views/policy/privacy-full.html</ns6:PrivacyStatementURL>
         </ns6:UIInfo>
      </ns0:Extensions>
      <ns0:KeyDescriptor use="signing">
         <ns7:KeyInfo>
            <ns7:X509Data>
               <ns7:X509Certificate>MIIDVzCCAj+gAwIBAgIJAN80zoFR2/UbMA0GCSqGSIb3DQEBCwUAMEIxCzAJBgNV BAYTAlhYMRUwEwYDVQQHDAxEZWZhdWx0IENpdHkxHDAaBgNVBAoME0RlZmF1bHQg Q29tcGFueSBMdGQwHhcNMTcwNDIxMDczMzA1WhcNMjcwNDIxMDczMzA1WjBCMQsw CQYDVQQGEwJYWDEVMBMGA1UEBwwMRGVmYXVsdCBDaXR5MRwwGgYDVQQKDBNEZWZh dWx0IENvbXBhbnkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA o87tb/hEU/igqFPtCFKMvC6LozTbH9y3I4lUVH38FDavDzrHAg1sVr5FEqguApeT xr/cmzsFMIB+XkAf9oI8xi2lUdorgeZFPFnUH0um4yXIJwBjrmgofUcybt84ee44 tM7AZKCAhinFDQUbjYV1LQP44QvFdGiklHGoo2NaVEqJwH6ce/8ioG5aFf2ISS6p fh3qOGVuQgansHFn+v+CvX+JU6FHB7mP+h3Xv+AoVjPz7b7E58rxn9qspy/N4LbB iDk7iBidsXEWYwYsSVP2cTrgKFktn5tB4YYZe0pSZNoCeVq05RK7kBy8yYCWTVZN Emkz5avL9Z2SDaGLY/9CTwIDAQABo1AwTjAdBgNVHQ4EFgQUrdY8o4OeseOy7ReD ZEZCKUZTk2gwHwYDVR0jBBgwFoAUrdY8o4OeseOy7ReDZEZCKUZTk2gwDAYDVR0T BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAoaygm+5U4j3/djWGQulXS2gdrPJV AS8zBuzQPVkhH76WcD8wxzuoceM80jPWLcP6Eq5Tma7rrqOE+QHrY8bm7LIYUEn2 fK/whozFyZ+TswEaDRjN6wL/FDuhu472Lnsg3rvE6s0eW1nlOHuqmqBQPb/kIMOj B3KOI6pqEfb+FqiZ2J/u/4KiOWaA8X9JQUo+HzWNEAPnNUoTl/yGr0Ad6z9YFbsu VnvJVTtGcu8pB5cjm7UtfN73ywEm/a/QXplus0U/Kv5XsSqaGa/Gw6pyX8LOc2yq I0XyOzj7DUcvMVZr5Vf/FVO2Od0Pb03+Wv4JRB5vXM1MsU+xAVgCm0pfew==</ns7:X509Certificate>
            </ns7:X509Data>
         </ns7:KeyInfo>
      </ns0:KeyDescriptor>
      <ns0:KeyDescriptor use="encryption">
         <ns7:KeyInfo>
            <ns7:X509Data>
               <ns7:X509Certificate>MIIDVzCCAj+gAwIBAgIJAN80zoFR2/UbMA0GCSqGSIb3DQEBCwUAMEIxCzAJBgNV BAYTAlhYMRUwEwYDVQQHDAxEZWZhdWx0IENpdHkxHDAaBgNVBAoME0RlZmF1bHQg Q29tcGFueSBMdGQwHhcNMTcwNDIxMDczMzA1WhcNMjcwNDIxMDczMzA1WjBCMQsw CQYDVQQGEwJYWDEVMBMGA1UEBwwMRGVmYXVsdCBDaXR5MRwwGgYDVQQKDBNEZWZh dWx0IENvbXBhbnkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA o87tb/hEU/igqFPtCFKMvC6LozTbH9y3I4lUVH38FDavDzrHAg1sVr5FEqguApeT xr/cmzsFMIB+XkAf9oI8xi2lUdorgeZFPFnUH0um4yXIJwBjrmgofUcybt84ee44 tM7AZKCAhinFDQUbjYV1LQP44QvFdGiklHGoo2NaVEqJwH6ce/8ioG5aFf2ISS6p fh3qOGVuQgansHFn+v+CvX+JU6FHB7mP+h3Xv+AoVjPz7b7E58rxn9qspy/N4LbB iDk7iBidsXEWYwYsSVP2cTrgKFktn5tB4YYZe0pSZNoCeVq05RK7kBy8yYCWTVZN Emkz5avL9Z2SDaGLY/9CTwIDAQABo1AwTjAdBgNVHQ4EFgQUrdY8o4OeseOy7ReD ZEZCKUZTk2gwHwYDVR0jBBgwFoAUrdY8o4OeseOy7ReDZEZCKUZTk2gwDAYDVR0T BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAoaygm+5U4j3/djWGQulXS2gdrPJV AS8zBuzQPVkhH76WcD8wxzuoceM80jPWLcP6Eq5Tma7rrqOE+QHrY8bm7LIYUEn2 fK/whozFyZ+TswEaDRjN6wL/FDuhu472Lnsg3rvE6s0eW1nlOHuqmqBQPb/kIMOj B3KOI6pqEfb+FqiZ2J/u/4KiOWaA8X9JQUo+HzWNEAPnNUoTl/yGr0Ad6z9YFbsu VnvJVTtGcu8pB5cjm7UtfN73ywEm/a/QXplus0U/Kv5XsSqaGa/Gw6pyX8LOc2yq I0XyOzj7DUcvMVZr5Vf/FVO2Od0Pb03+Wv4JRB5vXM1MsU+xAVgCm0pfew==</ns7:X509Certificate>
            </ns7:X509Data>
         </ns7:KeyInfo>
      </ns0:KeyDescriptor>
      <ns0:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://api.etais.ee/api-auth/saml2/logout/complete/" />
      <ns0:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://api.etais.ee/api-auth/saml2/logout/complete/" />
      <ns0:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://api.etais.ee/api-auth/saml2/login/complete/" index="1" />
      <ns0:AttributeConsumingService index="1">
         <ns0:ServiceName xml:lang="en">ETAIS Self-Service</ns0:ServiceName>
         <ns0:RequestedAttribute Name="urn:mace:dir:attribute-def:cn" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="cn" isRequired="true" />
         <ns0:RequestedAttribute Name="urn:oid:0.9.2342.19200300.100.1.3" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="mail" isRequired="true" />
         <ns0:RequestedAttribute Name="schacPersonalUniqueID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" isRequired="true" />
         <ns0:RequestedAttribute Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.6" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="eduPersonPrincipalName" isRequired="true" />
         <ns0:RequestedAttribute Name="schacHomeOrganization" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" isRequired="false" />
         <ns0:RequestedAttribute Name="urn:oid:2.16.840.1.113730.3.1.39" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="preferredLanguage" isRequired="false" />
         <ns0:RequestedAttribute Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.9" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="eduPersonScopedAffiliation" isRequired="false" />
      </ns0:AttributeConsumingService>
   </ns0:SPSSODescriptor>
   <ns0:Organization>
      <ns0:OrganizationName xml:lang="et">ETAIS</ns0:OrganizationName>
      <ns0:OrganizationName xml:lang="en">ETAIS</ns0:OrganizationName>
      <ns0:OrganizationDisplayName xml:lang="et">ETAIS</ns0:OrganizationDisplayName>
      <ns0:OrganizationDisplayName xml:lang="en">ETAIS</ns0:OrganizationDisplayName>
      <ns0:OrganizationURL xml:lang="et">http://etais.ee/</ns0:OrganizationURL>
      <ns0:OrganizationURL xml:lang="en">http://etais.ee/</ns0:OrganizationURL>
   </ns0:Organization>
   <ns0:ContactPerson contactType="technical">
      <ns0:GivenName>Administrator</ns0:GivenName>
      <ns0:EmailAddress>etais@etais.ee</ns0:EmailAddress>
   </ns0:ContactPerson>
</ns0:EntityDescriptor>
```

## Adding trusted identity providers

In order to configure Waldur to use SAML2 authentication you should specify identity provider metadata.

- If metadata XML is stored locally, it is cached in the local SQL database. Usually metadata XML file is big, so it
  is necessary to use local cache in this case. But you should ensure that metadata XML file is refreshed via cron
  on a regular basis. A management command ``waldur sync_saml2_providers`` performs refreshing of the data.
- If metadata XML is accessed remotely, it is not cached in SQL database. Therefore you should ensure that metadata
  XML is small enough. In this case you should download metadata signing certificate locally and specify its path in
  Waldur configuration. The certificate is used to retrieve the metadata securely. Please note that security
  certificates are updated regularly, therefore you should update configuration whenever certificate is updated.
  By convention, both metadata signing certificate and metadata itself are downloaded to ``/etc/waldur/saml2`` in
  Waldur Mastermind instances.

## References

### TAAT configuration

TaaT certificates can be downloaded from: [http://taat.edu.ee/main/dokumendid/sertifikaadid/](http://taat.edu.ee/main/dokumendid/sertifikaadid/).

Metadata URL for test hub is [https://reos.taat.edu.ee/saml2/idp/metadata.php](https://reos.taat.edu.ee/saml2/idp/metadata.php)
and for production hub is [https://sarvik.taat.edu.ee/saml2/idp/metadata.php](https://sarvik.taat.edu.ee/saml2/idp/metadata.php).
Note, the certificate must correspond to the hub you want connect to.

#### Using Janus

[Janus](https://taeva.taat.edu.ee/module.php/janus/index.php) is a self-service for managing Service Provider records.

- Create a new connection:

[![Janus](img/janus-add-new.png)](img/janus-add-new.png)

New connection ID must be equal to the base_url in saml.conf.py + /apu-auth/saml2/metadata/

- Choose SAML 2.0 SP for connection type.
- Click Create button
- In connection tab select or create ARP. Fields that ARP include must be in the saml_attribute_mapping.
- Navigate to the Import metadata tab and paste same URL as in the first step. Click on the Get metadata.
- Navigate to the Validate tab and check whether all the tests pass. You can fix metadata in Metadata tab.

## HAKA configuration

Production hub metadata is described at [https://wiki.eduuni.fi/display/CSCHAKA/Haka+metadata](https://wiki.eduuni.fi/display/CSCHAKA/Haka+metadata).

Test hub metadata is described at [https://wiki.eduuni.fi/display/CSCHAKA/Verifying+Haka+compatibility](https://wiki.eduuni.fi/display/CSCHAKA/Verifying+Haka+compatibility).

## FEDI configuration

Production hub metadata is described at [https://fedi.litnet.lt/en/metadata](https://fedi.litnet.lt/en/metadata).

Discovery is supported: [https://discovery.litnet.lt/simplesaml/module.php/discopower/disco.php](https://discovery.litnet.lt/simplesaml/module.php/discopower/disco.php).
