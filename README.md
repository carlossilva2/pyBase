<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="heading">

<tbody>

<tr bgcolor="#7799ee">

<td valign="bottom">   
<font color="#ffffff" face="helvetica, arial">   
<big><big>**pyBase**</big></big></font></td>

</tr>

</tbody>

</table>

<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="section">

<tbody>

<tr bgcolor="#ee77aa">

<td colspan="3" valign="bottom">   
<font color="#ffffff" face="helvetica, arial"><big>**Classes**</big></font></td>

</tr>

<tr>

<td bgcolor="#ee77aa"></td>

<td> </td>

<td width="100%">

<dl>

<dt><font face="helvetica, arial">Index:</font></dt>

<dd>

<dl>

<dt><font face="helvetica, arial">[Record](pyBase.html#Record)</font></dt>

<dt><font face="helvetica, arial">[pyBase](pyBase.html#pyBase)</font></dt>

</dl>

</dd>

</dl>

<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="section">

<tbody>

<tr bgcolor="#ffc8d8">

<td colspan="3" valign="bottom">   
<font color="#000000" face="helvetica, arial"><a name="Record">class **Record**</a>()</font></td>

</tr>

<tr bgcolor="#ffc8d8">

<td rowspan="2"></td>

<td colspan="2"><tt>[Record](#Record)(database=None)  

 </tt></td>

</tr>

<tr>

<td> </td>

<td width="100%">Methods defined here:  

<dl>

<dt><a name="Record-addOrQuery">**addOrQuery**</a>(self, field: str, operator, condition) -> object</dt>

</dl>

<dl>

<dt><a name="Record-addQuery">**addQuery**</a>(self, field: str, operator, condition) -> object</dt>

<dd><tt>Filter data by field and by providing a value</tt></dd>

</dl>

<dl>

<dt><a name="Record-delete">**delete**</a>(self) -> None</dt>

<dd><tt>DEPRECATED METHOD</tt></dd>

</dl>

<dl>

<dt><a name="Record-get">**get**</a>(self, id: str, p=False) -> pyBase.pyBase</dt>

<dd><tt>Returns a single database entry  

@param id - Unique record ID  

@param p - Flag for formated print  

@returns [pyBase](#pyBase) Object</tt></dd>

</dl>

<dl>

<dt><a name="Record-insert">**insert**</a>(self, json_data: dict) -> str</dt>

<dd><tt>Inserts [Record](#Record) in Database  

@param json_data dict</tt></dd>

</dl>

<dl>

<dt><a name="Record-mark_delete">**mark_delete**</a>(self, data: dict) -> object</dt>

<dd><tt>DEPRECATED METHOD</tt></dd>

</dl>

<dl>

<dt><a name="Record-query">**query**</a>(self, p=False) -> None</dt>

<dd><tt>Returns the results of a database with/without filter options and stores in "result" variable  

@param p - Flag for formated print  

@returns None</tt></dd>

</dl>

<dl>

<dt><a name="Record-setLimit">**setLimit**</a>(self, limit: int) -> None</dt>

<dd><tt>Set the number of [Record](#Record) returned  
@param limit - Number of records</tt></dd>

</dl>

<dl>

<dt><a name="Record-sort_by">**sort_by**</a>(self, field: str, order: str) -> object</dt>

<dd><tt>Set the order of the list  

@param field - Field of a Database  

@param order - If order is Ascending or Descending</tt></dd>

</dl>

</td>

</tr>

</tbody>

</table>

<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="section">

<tbody>

<tr bgcolor="#ffc8d8">

<td colspan="3" valign="bottom">   
<font color="#000000" face="helvetica, arial"><a name="pyBase">class **pyBase**</a>()</font></td>

</tr>

<tr bgcolor="#ffc8d8">

<td rowspan="2"></td>

<td colspan="2"><tt>[pyBase](#pyBase)(record=None, database=None, index=None)  

 </tt></td>

</tr>

<tr>

<td> </td>

<td width="100%">Methods defined here:  

<dl>

<dt><a name="pyBase-delete">**delete**</a>(self) -> None</dt>

<dd><tt>Permanently deletes [Record](#Record) from database</tt></dd>

</dl>

<dl>

<dt><a name="pyBase-getCreationTime">**getCreationTime**</a>(self)</dt>

<dd><tt>Returns date of [Record](#Record) creation</tt></dd>

</dl>

<dl>

<dt><a name="pyBase-update">**update**</a>(self) -> None</dt>

<dd><tt>Permanently saves [Record](#Record) changes in Database</tt></dd>

</dl>

<dl>

<dt><a name="pyBase-updateTime">**updateTime**</a>(self)</dt>

<dd><tt>Returns last update date</tt></dd>

</dl>

* * *

Static methods defined here:  

<dl>

<dt><a name="pyBase-getConfigPath">**getConfigPath**</a>()</dt>

<dd><tt>Returns [pyBase](#pyBase) local path</tt></dd>

</dl>

<dl>

<dt><a name="pyBase-getDBInfo">**getDBInfo**</a>(db: str) -> None</dt>

<dd><tt>Get DB structure</tt></dd>

</dl>

<dl>

<dt><a name="pyBase-getDatabases">**getDatabases**</a>() -> list</dt>

<dd><tt>Get databases in local system</tt></dd>

</dl>

</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="section">

<tbody>

<tr bgcolor="#eeaa77">

<td colspan="3" valign="bottom">   
<font color="#ffffff" face="helvetica, arial"><big>**Functions**</big></font></td>

</tr>

<tr>

<td bgcolor="#eeaa77"></td>

<td> </td>

<td width="100%">

<dl>

<dt><a name="-create_database_from_schema">**create_database_from_schema**</a>(verbose=False)</dt>

</dl>

<dl>

<dt><a name="-create_new_database">**create_new_database**</a>(name, verbose=True)</dt>

<dd><tt>Method to create new database</tt></dd>

</dl>

<dl>

<dt><a name="-encrypt">**encrypt**</a>(*args, **kwargs)</dt>

<dd><tt>Method to encrypt data</tt></dd>

</dl>

<dl>

<dt><a name="-load_data">**load_data**</a>(db)</dt>

<dd><tt>Loads data from a DB  
@param db - Name of Database  
@returns JSON dict</tt></dd>

</dl>

<dl>

<dt><a name="-save">**save**</a>(data, where)</dt>

<dd><tt>Save json data</tt></dd>

</dl>

</td>

</tr>

</tbody>

</table>