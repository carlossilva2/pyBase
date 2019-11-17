import json
from hashlib import md5, sha256, sha512
from time import time, ctime
from os import listdir, mkdir, system
import os.path as path
from copy import deepcopy
from random import randint
from terminaltables import AsciiTable
from codecs import encode, decode

colors = {
    "DONE": '\033[0;30;42m',
    'INFO': '\033[0;30;44m',
    "ERROR": '\033[0;30;41m',
    "WARNING": '\033[0;30;43m',
    "done": '\033[0;32;40m',
    "info": '\033[0;34;40m',
    "error": '\033[0;31;40m',
    "warning": '\033[0;33;40m',
    "normal": '\033[0;37;40m'
}

def save(data,where):
    "Save json data"
    try:
        with open(f"{path.expanduser('~')}/.pyBase/DBs/{where}", "wb") as outfile:
            data = json.dumps(data)
            data = encode(bytes(data.encode('utf-8')), "base64")
            outfile.write(data)
    except Exception as e:
        print(e.errno)

def encrypt(*args,**kwargs):
    "Method to encrypt data"
    if 'method' not in kwargs:
        raise AttributeError("You must specify a method to encrypt")
    try:
        method = eval(kwargs['method'])
    except Exception:
        exit(1)
    string = ""
    for item in args:
        string += str(item)
    return method(string.encode("UTF-8")).hexdigest()

def load_data(db):
    "Loads data from a DB\n@param db - Name of Database\n@returns JSON dict"
    database = "{}{}".format(str(db)[0:1].upper(),str(db)[1:].lower())
    if database not in [str(l).replace('.db','') for l in listdir(f'{path.expanduser("~")}/.pyBase/DBs')]:
        print(f"{colors['ERROR']} Error {colors['error']}  There is no such Database{colors['normal']}")
        exit(404)
    with open(f"{path.expanduser('~')}/.pyBase/DBs/{db}.db", "rb") as infile:
        check = infile.read()
        if len(check) == 0:
            print(f"{colors['WARNING']}WARNING{colors['warning']} Database is empty{colors['normal']}")
            return []
        return json.loads(decode(bytes(check), "base64").decode("utf-8"))

def create_new_database(name,verbose=True):
    "Method to create new database"
    open(f'{path.expanduser("~")}/.pyBase/DBs/{name}.db','w')
    if verbose:
        print('Database created')

def create_database_from_schema(verbose=False):
    if "Schemas" not in listdir(f"{path.expanduser('~')}/.pyBase"):
        print(f"{colors['ERROR']} ERROR {colors['error']}  Schema folder not present")
        if verbose: print(f"{colors['INFO']} INFO {colors['info']}  Creating folder...")
        mkdir(f"{path.expanduser('~')}/.pyBase/Schemas")
        if verbose: print(f"{colors['INFO']} INFO {colors['info']}  Please create a schema.json file before proceeding")
        exit(1)
    if "schema.json" not in listdir(f"{path.expanduser('~')}/.pyBase/Schemas"):
        print(f"{colors['ERROR']} ERROR {colors['error']}  schema.json file not present")
        exit(1)
    schema = json.load(open(f'{path.expanduser("~")}/.pyBase/Schemas/schema.json', 'r'))
    keys = schema.keys()
    direct = [str(l).replace('.db','') for l in listdir(f"{path.expanduser('~')}/.pyBase/DBs")]
    for key in keys:
        if verbose: print(f"{colors['INFO']} INFO {colors['info']}  Creating {key}.db")
        if key not in direct:
            save([],f"{key}.db")

class pyBase:

    def __init__(self, record=None, database=None, index=None):
        self.__slots__ = list(record.keys())
        self.__dict__['database'] = database
        self.__dict__['index'] = index
        self.__dict__['raw'] = record
        for key in self.__slots__:
            self.__dict__[key] = record[key]
        self.schema = json.load(open(f'{path.expanduser("~")}/.pyBase/Schemas/schema.json', 'r'))[self.database]

    def __repr__(self):
        return '[object Object]'

    #PUBLIC METHODS

    def getCreationTime(self):
        "Returns date of Record creation"
        s = str(self.__dict__['created']).split('.')[0]
        return ctime(int(s))
    
    def updateTime(self):
        "Returns last update date"
        s = str(self.__dict__['updated']).split('.')[0]
        return ctime(int(s)) 
    
    def update(self) -> None:
        "Permanently saves Record changes in Database"
        try:
            block = {}
            data = load_data(self.database)
            for key in self.__slots__:
                typecheck = self.__check_type(self.__dict__,key,self.schema)
                if typecheck[0]:
                    block[key] = self.__dict__[key]
                else:
                    print(f"{colors['ERROR']} Error {colors['error']}  {key} field must be {typecheck[1]}, {typecheck[2]} was inserted{colors['normal']}")
                    exit(1)
            sys_cre = str(time())
            block['updated'] = sys_cre
            data[self.index] = block
            save(data,f"{self.database}.db")
        except Exception as e:
            print(str(e))
    
    def delete(self) -> None:
        "Permanently deletes Record from database"
        data = load_data(self.database)
        data.pop(self.index)
        save(data,f"{self.database}.db")
    
    #PRIVATE METHODS

    def __check_type(self,data: dict,key: str,schema: dict) -> bool:
        field_type = None
        value_type = None
        for field in self.schema['columns']:
            if field['name'] == key:
                field_type = field['type']
                value_type = str(type(data[field['name']])).replace('<class \'','').replace('\'>','')
                break
        return field_type == value_type, field_type, value_type

    #STATIC METHODS

    @staticmethod
    def getDatabases() -> list:
        "Get databases in local system"
        return [str(db).replace('.db','') for db in list(listdir(f"{path.expanduser('~')}/.pyBase/DBs"))]
    
    @staticmethod
    def getDBInfo(db: str) -> None:
        "Get DB structure"
        database = "{}{}".format(str(db)[0:1].upper(),str(db)[1:].lower())
        if database not in [str(l).replace('.db','') for l in listdir(f'{path.expanduser("~")}/.pyBase/DBs')]:
            print(f"{colors['ERROR']} Error {colors['error']}  There is no such Database{colors['normal']}")
            exit(404)
        schema = json.load(open(f'{path.expanduser("~")}/.pyBase/Schemas/schema.json', 'r'))[database]
        to_print =[]
        to_print.append(["Name", "Type"])
        for column in schema['columns']:
            data = [column['name'],column['type']]
            to_print.append(data)
        system('clear')
        print(AsciiTable(to_print).table, flush=True)
    
    @staticmethod
    def getConfigPath():
        "Returns pyBase local path"
        return f"{path.expanduser('~')}/.pyBase"

class Record:

    GREATER_THAN = "greater than"
    GREATER = "greater"
    LESS_THAN = "less than"
    LESS = "less"
    EQUALS = "equals"
    CONTAINS = "contains"
    ISNULL = "isNull"
    STARTS_WITH = "starts with"
    ENDS_WITH = "ends with"

    def __init__(self, database=None):
        "Constructor"
        if not database:
            raise Exception("Database name is mandatory")
        #PUBLIC VARIABLES
        self.database = "{}{}".format(str(database)[0:1].upper(),str(database)[1:].lower())
        if self.database not in [str(l).replace('.db','') for l in listdir(f'{path.expanduser("~")}/.pyBase/DBs')]:
            print(f"{colors['ERROR']} Error {colors['error']}  There is no such Database{colors['normal']}")
            exit(404)
        self.schema = json.load(open(f'{path.expanduser("~")}/.pyBase/Schemas/schema.json', 'r'))[self.database]
        self.data = load_data(database)
        self.results = []
        self.result = None
        self.count = None
        self.metric = time()

        #PRIVATE VARIABLES
        self.__ordered = {
            "Field": None,
            "Ordered": False,
            "Order": "Desc"
        }
        self.__to_delete = []
        self.__limit = None
    
    def __repr__(self):
        "Repr"
        return f"{self.database} - {len(self.data)} results\n{colors['INFO']}Fields{colors['normal']} - {[x['name'] for x in self.schema['columns']]}"

    #PUBLIC METHODS
    
    def addQuery(self,field: str,operator,condition) -> object:
        "Filter data by field and by providing a value"
        if len(self.results) == 0:
            for item in self.data:
                keys = item.keys()
                if field in keys:
                    if self.__do_comparison(field,item[field],operator,condition):
                        self.results.append(item)

            self.count = len(self.results)
        else:
            res = deepcopy(self.results)
            self.results = []
            for item in res:
                keys = item.keys()
                if field in keys:
                    result = self.__do_comparison(field,item[field],operator,condition)
                    if result:
                        self.results.append(item)
            
            self.count = len(self.results)
        return self

    def addOrQuery(self,field: str,operator,condition) -> object:
        for item in self.data:
            keys = item.keys()
            if field in keys:
                if self.__do_comparison(field,item[field],operator,condition):
                    self.results.append(item)
        
        self.count = len(self.results)
        return self
    
    def get(self, id: str, p=False) -> pyBase:
        """
        Returns a single database entry\n
        @param id - Unique record ID\n
        @param p - Flag for formated print\n
        @returns pyBase Object
        """
        for item in self.data:
            if item['id'] == id:
                if p:
                    headers = [str(key) for key in item.keys()]
                    content = [str(item[key]) for key in headers]
                    print(AsciiTable([headers,content]).table, flush=True)
                return pyBase(item,self.database, self.data.index(item))
        return None

    def delete(self) -> None:
        "DEPRECATED METHOD"
        print(f"{colors['WARNING']}WARNING{colors['warning']} Deprecated method{colors['normal']}")
        start = time()
        deletion = []
        ids = [x['id'] for x in self.data]
        for index, item in enumerate(self.__to_delete):
            if item in ids:
                deletion.append(index)
        deletion.sort()
        deletion.reverse()
        for i in deletion:
            self.data.pop(i)
        save(self.data, f"{self.database}.db")
        end = time()
        print(f"{colors['INFO']}INFO{colors['info']} Deleted {len(deletion)} records in {end-start}s")
    
    def mark_delete(self, data: dict) -> object:
        "DEPRECATED METHOD"
        print(f"{colors['WARNING']}WARNING{colors['warning']} Deprecated method{colors['normal']}")
        self.__to_delete.append(data.id)
        return self

    def query(self, p=False) -> None:
        """
        Returns the results of a database with/without filter options and stores in "result" variable\n
        @param p - Flag for formated print\n
        @returns None
        """
        self.result = []
        if len(self.results) > 0:
            keys = self.results[0].keys()
            to_print =[]
            to_print.append([key for key in keys])
            to_print[0].insert(0,"index")
            i = 0
            dupes = []
            if len(dupes) > 0:
                dupes.sort()
                dupes.reverse()
                for x in dupes:
                    self.results.pop(x)
            if self.__ordered['Ordered']:
                self.results = sorted(self.results, key=lambda x : x[self.__ordered['Field']])
                if self.__ordered['Order'] == "Desc":
                    self.results.reverse()
            for item in (self.results if self.__limit == None else self.results[:self.__limit]):
                block = {}
                data = [i]
                for key in keys:
                    block[key] = item[key]
                    data.append(item[key])
                self.result.append(pyBase(item,self.database,self.data.index(item)))
                to_print.append(data)
                i += 1
            self.count = len(self.result)
            if p:
                system('clear')
                print(AsciiTable(to_print).table, flush=True)
        else:
            keys = self.data[0].keys()
            to_print =[]
            to_print.append([key for key in keys])
            to_print[0].insert(0,"index")
            i = 0
            if self.__ordered['Ordered']:
                self.data = sorted(self.data, key=lambda x : x[self.__ordered['Field']])
                if self.__ordered['Order'] == "Desc":
                    self.data.reverse()
            for item in (self.data if self.__limit == None else self.data[:self.__limit]):
                block = {}
                data = [i]
                for key in keys:
                    block[key] = item[key]
                    data.append(item[key])
                self.result.append(pyBase(item,self.database,self.data.index(item)))
                to_print.append(data)
                i += 1
            self.count = len(self.result)
            if p:
                system('clear')
                print(AsciiTable(to_print).table, flush=True)
        self.metric = f'{round(time() - self.metric,4)}s'
    
    def insert(self, json_data: dict) -> str:
        """
        Inserts Record in Database\n
        @param json_data - dict
        """
        return self.__insert(self.schema, json_data)
    
    def sort_by(self, field: str, order: str) -> object:
        """Set the order of the list\n
        @param field - Field of a Database\n
        @param order - If order is Ascending or Descending"""
        order = order or "Desc"
        self.__ordered["Field"] = field
        self.__ordered["Ordered"] = True
        self.__ordered["Order"] = order
        return self
    
    def setLimit(self, limit: int) -> None:
        "Set the number of Record returned\n@param limit - Number of records"
        self.__limit = limit if limit >= 1 else 1
        return self

    #PRIVATE METHODS
    
    def __insert(self,schema, json_data):
        allowed = self.__check_missing(json_data,schema)
        keys = json_data.keys()
        block = {}
        block['id'] = encrypt(time(),self.database,json_data,'PYBASE',method="md5")
        sys_creation = str(time())
        block['created'] = sys_creation
        block['updated'] = sys_creation
        for i in allowed:
            block[i] = None
        for key in keys:
            item = None
            for index, field in enumerate(schema['columns']):
                if field['name'] == key:
                    item = field
                    break
            optionals = item['optional'][0] if "optional" in item else None
            if optionals and "allow_empty" in optionals:
                if optionals['allow_empty'] == "no" and (json_data[item['name']] is None or json_data[item['name']] == ""):
                    print(f"{colors['ERROR']} Error {colors['error']}  {item['name']} field cannot be empty{colors['normal']}")
                    exit(1)
            typecheck = self.__check_type(json_data,key,schema)
            if typecheck[0]:
                block[key] = json_data[key]
            else:
                print(f"{colors['ERROR']} Error {colors['error']}  {key} field must be {typecheck[1]}, {typecheck[2]} was inserted{colors['normal']}")
                exit(1)
        self.data.append(block)
        save(self.data,f"{self.database}.db")
        return block['id']
    
    def __check_missing(self, data, schema):
        item = []
        allowed = []
        for field in schema['columns']:
            optionals = field['optional'] if "optional" in field else None
            if field['name'] not in data.keys() and field['name'] != "id":
                if optionals is not None and optionals[0]['allow_empty'] == "no":
                    item.append(field['name'])
                else:
                    allowed.append(field['name'])
        if len(item) > 0:
            for i in item:
                print(f"{colors['ERROR']} Error {colors['error']}  {i} field cannot be empty{colors['normal']}")
            exit(1)
        return allowed
    
    def __check_type(self,data,key,schema):
        field_type = None
        value_type = None
        for field in schema['columns']:
            if field['name'] == key:
                field_type = field['type']
                value_type = str(type(data[field['name']])).replace('<class \'','').replace('\'>','')
                break
        return field_type == value_type, field_type, value_type
    
    def __do_comparison(self,name,data,operator,value):
        index = None
        for i, fields in enumerate(self.schema['columns']):
            if fields['name'] == name:
                index = i
                break
        field_type = self.schema['columns'][index]['type']
        value_type = str(type(value)).replace('<class \'','').replace('\'>','')
        if field_type != value_type and operator != "isNull":
            if operator in ['less', 'greater', 'less than', 'greater than', 'equals'] and field_type == "str" and value_type == "int":
                pass
            else:
                return None
        if operator == "less":
            if field_type == "str":
                return len(data) < value
            return eval(field_type)(data) < value
        
        elif operator == "less than":
            if field_type == "str":
                return len(data) <= value
            return eval(field_type)(data) <= value
        
        elif operator == "greater than":
            if field_type == "str":
                return len(data) >= value
            return eval(field_type)(data) >= value

        elif operator == "greater":
            if field_type == "str":
                return len(data) > value
            return eval(field_type)(data) > value
        
        elif operator == "equals":
            if field_type == "str" and value_type == "int":
                return len(data) == value
            return value == eval(field_type)(data)
        
        elif operator == "contains":
            return value in eval(field_type)(data)
        
        elif operator == "isNull":
            return data == None
        
        elif operator == "starts with":
            chars = len(value)
            s = str(data)[:chars]
            return s == value

        elif operator == "ends with":
            chars = len(value)
            s = str(data)[len(data)-chars:]
            return s == value
        
        else:
            raise Exception("Operator is not supported")
    
    def __check_for_dups(self,data):
        seen = {}
        dupes = []
        for index, item in enumerate(data):
            if item['id'] not in seen:
                seen[item['id']] = 1
            else:
                if seen[item['id']] >= 1:
                    dupes.append(index)
                seen[item['id']] += 1
        return dupes
