.. Shared diagram: included by using/external-connections/external-identity-sources/file-source.rst
   and getting-started/connections/source-hr-file.rst. Edit here to change both.

.. code-block:: text

   System of record ──export──▶ CSV file on the Registry server
                                        │
                              Sync Job or manual sync
                                        ▼
                     External Identity Source (File Source)
                       each row becomes an External Identity
                                        │
                                     Pipeline
                    (flanges can add capabilities, such as a login)
                                        ▼
                         Person record and Person Roles
