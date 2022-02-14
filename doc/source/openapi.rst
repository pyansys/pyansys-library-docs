OpenAPI Common Library
----------------------
The ``openapi-common`` repository provides the source code for
authentication-aware clients for OpenAPI client libraries.

The PyAnsys Open API Common library is intended for use with the custom code
generation template in the `PyAnsys project <https://github.com/pyansys>`_.
This library currently supports authentication with Basic, Negotiate, NTLM,
and OpenID Connect. Most features of the underlying requests session are
exposed for use. Some basic configuration is also provided by default.

Installation
~~~~~~~~~~~~

Install ``openapi-common`` with:

.. code::

   pip install ansys-openapi-common

Usage
~~~~~
The package exposes several classes, including a client
:py:class:`~ansys.openapi.common.ApiClient` and a builder
:py:class:`~ansys.openapi.common.ApiClientFactory` that allow a client library
to configure a connection to an API.

The :py:class:`~ansys.openapi.common.ApiClient` class is intended to be wrapped
by code that implements a client library.

Authentication is configured through the
:py:class:`~ansys.openapi.common.ApiClientFactory` object and its
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_credentials`,
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_autologon`, and
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_oidc` methods. If no
authentication is required, you can use the
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_anonymous` method. You can
provide additional configuration with the
:py:class:`~ansys.openapi.common.SessionConfiguration` object.

.. code:: python

   >>> from ansys.openapi.common import ApiClientFactory
   >>> session = ApiClientFactory('https://my-api.com/v1.svc')
   ...           .with_autologon()
   ...           .connect()
   <ApiClient url: https://my-api.com/v1.svc>

Resources and Links
~~~~~~~~~~~~~~~~~~~
For more information, see:

  - :external+openapi-common:doc:`OpenAPI-Common Documentation <index>`
  - `OpenAPI-Common PyPI <https://pypi.org/project/ansys-openapi-common/>`_
  - `OpenAPI-Common GitHub <https://github.com/pyansys/openapi-common/>`_
