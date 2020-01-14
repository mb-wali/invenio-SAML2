# Invenio SAML
  Module for invenio that provides authentication via Shibboleth.
  
## Installation

### Requirments
The python3-saml module uses ```xmlsec```, which offers Python bindings for the XML Security Library. ```xmlsec``` depends on ```libxml2-dev``` and ```libxmlsec1-dev```. These libraries can be installed via the package manager of your distribution. For Ubuntu use:

```
$ sudo apt install libxml2-dev libxmlsec1-dev
```

also add this script in your ```Dockerfile.base``` just after FROM inveniosoftware/centos7-python:3.6 line.

```
RUN yum -y install libxml2-devel xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel
```

### invenio-SAML

invenio-SAML module can be installed as bellow:

Add this to your invenio Pipfile

```
invenio-SAML = { git = 'https://github.com/mb-wali/invenio-SAML.git', editable = 'true' }
```

## Run
```
pipenv install
```
---

## Configuration

### config.py

Visit <https://www.samltool.com/self_signed_certs.php> to generate self signed ```sp.crt``` and ```sp.key```.

sp.crt (X.509 cert) The public cert of the SP. 
```
SHIBBOLETH_SERVICE_PROVIDER_CERTIFICATE = './docker/shibbolethAuthenticator/sp.crt'
```

sp.key (Private key) The private key of the SP (Service Provider)
```
SHIBBOLETH_SERVICE_PROVIDER_PRIVATE_KEY = './docker/shibbolethAuthenticator/sp.key'
```

idp.crt The public cert of the IDP (Identity Provider)
```
SHIBBOLETH_IDP_CERT = './docker/shibbolethAuthenticator/idp.crt'
```

Number of seconds after which the state token expires
```
SHIBBOLETH_STATE_EXPIRES = 300
```

```
""" SERVICE_PROVIDER is your application in this case invenioRDM.
""" strict """
""" debug """
"""entity_id 'this can be a unique URI that the IDENTITY_PROVIDERS knows which Service provider is asking for
    identity' """
    
SHIBBOLETH_SERVICE_PROVIDER = dict(
    strict=True,
    debug=True,
    entity_id='https://mydomain/shibboleth'
)
```


```
""" IDENTITY_PROVIDERS is remote application which we redirect the user to login """
""" idp = dict() """ 'is name of your remote_app. this dictionary can have these values' 
                 """ entity_id """ 
                 """ title """ 
                 """ sso_url """ 'is URL you get from your remote application to redirect the user'.
                 """ mapping = dict() """ 'is the values or fields you get back from your remote application':
                     see below for examples:
                     
SHIBBOLETH_IDENTITY_PROVIDERS = dict(
    idp=dict(
        entity_id='https://identityprovider/idp/shibboleth',  # name of invenio something to get to know
        title='RDM remote application',
        sso_url='https://identityprovider/idp/profile/SAML2/Redirect/SSO',  # redirects to for authentication
        sso__Logout_url='https://sso.idp.com/slo/Logout', # Logout url 
        mappings=dict(
            email='urn:oid:0.9.2342.19200300.100.1.3',
            full_name='urn:oid:2.5.4.3',
            user_unique_id='urn:oid:2.16.756.1.2.5.1.1.1',
            .
            .
            .
        )
    )
)
```
---

## Blueprints
After successfull installation and configurtion.
you will be able to navigate to these endpoints.

* Metadata

Navigate to this endpoint to see your xml Metadata.
  ```
  https://yourdomanin.com/shibboleth/metadata/<remote_app>
  ```
---

* Login

Navigate to this endpoint to redirect the User to login with the SSO
  ```
  https://yourdomanin.com/shibboleth/login/<remote_app>
  ```
---

* Authorized

This endpoint is activated when the Identity Provider redirects back to Service Provider.

  ```
  https://yourdomanin.com/shibboleth/authorized/<remote_app>
  ```
