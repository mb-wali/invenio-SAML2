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

#### SERVICES_PROVIDER
```SHIBBOLETH_SERVICES_PROVIDER``` Is your application/Service in this case invenio.
- ```strict``` MUST be set as ```True```. Otherwise your environment is not secure and will be exposed to attacks.
- ```debug``` set this ```True``` for debugging purposes.
- ```entity_id``` is a unique self signed URI, with this the ```IDENTITY_PROVIDERS``` knows which ```SERVICES_PROVIDER``` is asking for identity.

see example below:

``` 
SHIBBOLETH_SERVICE_PROVIDER = dict(
    strict=True,
    debug=True,
    entity_id='https://mydomain/shibboleth'
)
```

#### IDENTITY_PROVIDERS
```SHIBBOLETH_IDENTITY_PROVIDERS``` Is remote application which we redirect the user to login or to identify.
- ```idp = dict()``` ```idp``` is your remote_app name, which has these below fields:
  - ```entity_id``` is a unique URI from your ```IDENTITY_PROVIDERS```.
  - ```title``` you can give a title for your ```idp``` [OPTIONAL]
  - ```sso_url``` is the URL to redirect the user. URL for ```IDENTITY_PROVIDERS```.
  - ```sso__Logout_url``` is the URL to redirect for logout.
  - ```mappings=dict()``` is the fields/values that ```IDENTITY_PROVIDERS``` sends back after successful identity of user.
    - ```email```
    - ```full_name```
    - ```user_unique_id```

see example below:

```
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
