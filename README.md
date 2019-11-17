# Index:

1. [Classes](#gen-class)
    1. [Record](#rec-class)
        * [Methods](#rec-meth)
            1. [addOrQuery](#Record-addOrQuery)
            1. [addQuery](#Record-addQuery)
            1. [delete](#Record-delete)
            1. [get](#Record-get)
            1. [insert](#Record-insert)
            1. [mark_delete](#Record-mark_delete)
            1. [query](#Record-query)
            1. [setLimit](#Record-setLimit)
            1. [sort_by](#Record-sort_by)

    2. [pyBase](#py-class)
        * [Methods](#py-meth)
            1. [delete](#pyBase-delete)
            1. [getCreationTime](#pyBase-getCreationTime)
            1. [update](#pyBase-update)
            1. [updateTime](#pyBase-updateTime)
            
        * [Static Methods](#py-static)
            1. [getConfigPath](#pyBase-getConfigPath)
            1. [getDBInfo](#pyBase-getDBInfo)
            1. [getDatabases](#pyBase-getDatabases)

3. [Functions](#gen-func)
    1. [create_database_from_schema](#-create_database_from_schema)
    1. [create_new_database](#-create_new_database)
    1. [encrypt](#-encrypt)
    1. [load_data](#-load_data)
    1. [save](#-save)

# **pyBase**

<a name="gen-class"></a>
## **Classes** 

<a name="rec-class"></a>
### class **Record**()

* [Record](#rec-class)(database=None)

<a name="rec-meth"></a>
#### Methods defined here:  

<a name="Record-addOrQuery"></a>
* **addOrQuery**(self, field: str, operator, condition) -> object

<a name="Record-addQuery"></a>
* **addQuery**(self, field: str, operator, condition) -> object

    `Filter data by field and by providing a value`

<a name="Record-delete"></a>
* **delete**(self) -> None

    `DEPRECATED METHOD`

<a name="Record-get"></a>
* **get**(self, id: str, p=False) -> [pyBase](#py-class)

    `Returns a single database entry`  

    1. @param id - Unique record ID  

    1. @param p - Flag for formated print  

    1. @returns [pyBase](#py-class) Object

<a name="Record-insert"></a>
* **insert**(self, json_data: dict) -> str

    `Inserts [Record](#Record) in Database`  

    1. @param json_data - dict

<a name="Record-mark_delete"></a>
* **mark_delete**(self, data: dict) -> object

    `DEPRECATED METHOD`

<a name="Record-query"></a>
* **query**(self, p=False) -> None

    `Returns the results of a database with/without filter options and stores in "result" variable`  

    1. @param p - Flag for formated print  

    1. @returns None

<a name="Record-setLimit"></a>
* **setLimit**(self, limit: int) -> None

    `Set the number of Records returned`  
    1. @param limit - Number of records

<a name="Record-sort_by"></a>
* **sort_by**(self, field: str, order: str) -> object

    `Set the order of the list`  

    1. @param field - Field of a Database  

    1. @param order - If order is Ascending or Descending


---

<a name="py-class"></a>
### class **pyBase**

* [pyBase](#py-class)(record=None, database=None, index=None)  

<a name="py-meth"></a>
#### Methods defined here:  

<a name="pyBase-delete"></a>
* **delete**(self) -> None

    `Permanently deletes Record from database`

<a name="pyBase-getCreationTime"></a>
* **getCreationTime**(self)

    `Returns date of Record creation`

<a name="pyBase-update"></a>
* **update**(self) -> None

    `Permanently saves Record changes in Database`

<a name="pyBase-updateTime"></a>
* **updateTime**(self)

    `Returns last update date`

---

<a name="py-static"></a>
Static methods defined here:  

<a name="pyBase-getConfigPath"></a>
* **getConfigPath**()

    `Returns pyBase local path`

<a name="pyBase-getDBInfo"></a>
* **getDBInfo**(db: str) -> None

    `Get DB structure`

<a name="pyBase-getDatabases"></a>
* **getDatabases**() -> list

    `Get databases in local system`
---

<a name="gen-func"></a>
### **Functions**

<a name="-create_database_from_schema"></a>
* **create_database_from_schema**(verbose=False)

<a name="-create_new_database"></a>
* **create_new_database**(name, verbose=True)

    `Method to create new database`

<a name="-encrypt"></a>
* **encrypt**(*args, **kwargs)

    `Method to encrypt data`

<a name="-load_data"></a>
* **load_data**(db)

    `Loads data from a DB`  
    1. @param db - Name of Database  
    1. @returns JSON dict

<a name="-save"></a>
* **save**(data, where)

    `Save json data`
