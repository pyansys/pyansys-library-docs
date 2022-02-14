PyAnsys Shared Components
=========================

As part of the PyAnsys project to enable the usage of Ansys
products through Python, we have created shared components
that are reusable across the different packages.

These shared components are not interfaces to specific products nor
single-purpose tools. They are libraries to facilitate code-sharing
within the project.

This is an expanding and developing project. Feel free
to post issues on the various GitHub pages in this document.
For additional support, contact `PyAnsys Support
<mailto:pyansys.support@ansys.com>`_, who will correctly route
your requests.

PyAnsys Shared Components
-------------------------
The ``pyansys-library-docs`` repository provides the source code for
libraries that faciliate code-sharing with the PyAnsys project.

The PyAnsys Shared Components library is intended for use with the custom code generation
template in the `PyAnsys project <https://github.com/pyansys>`_. 

Installation
~~~~~~~~~~~~

Install ``pyansys-library-docs`` with:

.. code::

   pip install pyansys-library-docs

Usage
~~~~~
The package exposes several classes, including a client :py:class:`~ansys.openapi.common.ApiClient` and a
builder :py:class:`~ansys.openapi.common.ApiClientFactory`, these allow a client
library to configure a connection to an API.

The :py:class:`~ansys.openapi.common.ApiClient` class is intended to be wrapped by code that implements 
a client library.

Authentication is configured through the :py:class:`~ansys.openapi.common.ApiClientFactory`
object and its :py:meth:`~ansys.openapi.common.ApiClientFactory.with_credentials`,
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_autologon`, and 
:py:meth:`~ansys.openapi.common.ApiClientFactory.with_oidc` methods. If no authentication 
is required, you can use the :py:meth:`~ansys.openapi.common.ApiClientFactory.with_anonymous` method.
You can provide additional configuration with the :py:class:`~ansys.openapi.common.SessionConfiguration` object.

.. code:: python

   >>> from ansys.openapi.common import ApiClientFactory
   >>> session = ApiClientFactory('https://my-api.com/v1.svc')
   ...           .with_autologon()
   ...           .connect()
   <ApiClient url: https://my-api.com/v1.svc>
   
Resources and Links
~~~~~~~~~~~~~~~~~~~
For more details, see:

  - `OpenAPI-Common Documentation <https://openapi.docs.pyansys.com/>`_
  - `OpenAPI-Common PyPI <https://pypi.org/project/ansys-openapi-common/>`_
  - `OpenAPI-Common GitHub <https://github.com/pyansys/openapi-common/>`_

