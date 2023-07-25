# All tables from Northwind Database
# An alternative would be using a SQL query to obtain table names, but would add an additional step to the pipeline
extraction_tables = ['categories',
                 'customer_customer_demo',
                 'customer_demographics',
                 'customers',
                 'employees',
                 'employee_territories',
                 'orders',
                 'products',
                 'region',
                 'shippers',
                 'suppliers',
                 'territories',
                 'us_states']

# All table columns that are added as index in the .csv files
table_columns = {'categories':['category_id', 'category_name', 'description', 'picture'],
                 'customer_customer_demo':['customer_id', 'customer_type_id'],
                 'customer_demographics':['customer_type_id', 'customer_desc'],
                 'customers': ['customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'],
                 'employees': ['employee_id', 'last_name', 'first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'photo', 'notes', 'reports_to', 'photo_path'],
                 'employee_territories' : ['employee_id', 'territory_id'],
                 'orders' : ['order_id', 'customer_id', 'employee_id', 'order_date', 'required_date', 'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city', 'ship_region', 'ship_postal_code', 'ship_country'],
                 'products' : ['product_id', 'product_name', 'supplier_id', 'category_id', 'quantity_per_unit', 'unit_price', 'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued'],
                 'region' : ['region_id', 'region_description'],
                 'shippers' : ['shipper_id', 'company_name', 'phone'],
                 'suppliers' : ['supplier_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax', 'homepage'],
                 'territories' : ['territory_id', 'territory_description', 'region_id'],
                 'us_states': ['state_id', 'state_name', 'state_abbr', 'state_region']}

# SQL Commands for database creation
table_creation = {
'categories' : '''CREATE TABLE categories (
                                                category_id smallint NOT NULL,
                                                category_name character varying(15) NOT NULL,
                                                description text,
                                                picture blob
                                            )''',

'customer_customer_demo' : '''CREATE TABLE customer_customer_demo (
                                                                    customer_id varchar(5) NOT NULL,
                                                                    customer_type_id varchar(5) NOT NULL
                                                                )''',
                                                                       
'customer_demographics' : '''CREATE TABLE customer_demographics (
                                                                    customer_type_id varchar(5) NOT NULL,
                                                                    customer_desc text
                                                                )''',
                                                                
'customers' : '''CREATE TABLE customers (
                                            customer_id varchar(5) NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            contact_name character varying(30),
                                            contact_title character varying(30),
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            phone character varying(24),
                                            fax character varying(24)
                                            )''',    
                                            
'employees' : '''CREATE TABLE employees (
                                            employee_id smallint NOT NULL,
                                            last_name character varying(20) NOT NULL,
                                            first_name character varying(10) NOT NULL,
                                            title character varying(30),
                                            title_of_courtesy character varying(25),
                                            birth_date date,
                                            hire_date date,
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            home_phone character varying(24),
                                            extension character varying(4),
                                            photo blob,
                                            notes text,
                                            reports_to smallint,
                                            photo_path character varying(255)
                                            )''',                   

'employee_territories' : '''CREATE TABLE employee_territories (
                                                                    employee_id smallint NOT NULL,
                                                                    territory_id character varying(20) NOT NULL
                                                                  )''',                                                                           
                                                                                                                                    
'orders' : '''CREATE TABLE orders (
                                        order_id smallint NOT NULL,
                                        customer_id varchar(5) NOT NULL,
                                        employee_id smallint NOT NULL,
                                        order_date date,
                                        required_date date,
                                        shipped_date date,
                                        ship_via smallint,
                                        freight real,
                                        ship_name character varying(40),
                                        ship_address character varying(60),
                                        ship_city character varying(15),
                                        ship_region character varying(15),
                                        ship_postal_code character varying(10),
                                        ship_country character varying(15),
                                        PRIMARY KEY (order_id)
                                    )''',

'products' : '''CREATE TABLE products (
                                            product_id smallint NOT NULL,
                                            product_name character varying(40) NOT NULL,
                                            supplier_id smallint,
                                            category_id smallint,
                                            quantity_per_unit character varying(20),
                                            unit_price real,
                                            units_in_stock smallint,
                                            units_on_order smallint,
                                            reorder_level smallint,
                                            discontinued integer NOT NULL
                                          )''',
                                          
'region' : '''CREATE TABLE region (
                                        region_id smallint NOT NULL,
                                        region_description text
                                      )''',   
                                      
'shippers' : '''CREATE TABLE shippers (
                                            shipper_id smallint NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            phone character varying(24)
                                          )''',    
                                          
'suppliers' : '''CREATE TABLE suppliers (
                                            supplier_id smallint NOT NULL,
                                            company_name character varying(40) NOT NULL,
                                            contact_name character varying(30),
                                            contact_title character varying(30),
                                            address character varying(60),
                                            city character varying(15),
                                            region character varying(15),
                                            postal_code character varying(10),
                                            country character varying(15),
                                            phone character varying(24),
                                            fax character varying(24),
                                            homepage text
                                            )''',   
                                            
'territories' : '''CREATE TABLE territories (
                                                territory_id character varying(20) NOT NULL,
                                                territory_description text NOT NULL,
                                                region_id smallint NOT NULL
                                                )''',       
                                                
'us_states' : '''CREATE TABLE us_states (
                                            state_id smallint NOT NULL,
                                            state_name character varying(100),
                                            state_abbr character varying(2),
                                            state_region character varying(50)
                                            )''',

'order_details' : '''CREATE TABLE order_details (
                                                    order_id smallint NOT NULL,
                                                    product_id smallint NOT NULL,
                                                    unit_price real,
                                                    quantity smallint,
                                                    discount real,
                                                    FOREIGN KEY (order_id) REFERENCES orders(order_id)
                                                    )'''                                                         
                                                   }

# Insertion SQL commands for the SQLite database
table_insert = { 'categories' : 'INSERT INTO categories VALUES (?, ?, ?, ?)',
                 'customer_customer_demo': 'INSERT INTO customer_customer_demo VALUES (?, ?)',
                 'customer_demographics' : 'INSERT INTO customer_demographics VALUES (?, ?)',
                 'customers' : 'INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 'employees' : 'INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 'employee_territories' : 'INSERT INTO employee_territories VALUES (?, ?)',
                 'orders' : 'INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 'products' : 'INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 'region' : 'INSERT INTO region VALUES (?, ?)',
                 'shippers' :'INSERT INTO shippers VALUES (?, ?, ?)',
                 'suppliers' : 'INSERT INTO suppliers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 'territories' : 'INSERT INTO territories VALUES (?, ?, ?)',
                 'us_states' : 'INSERT INTO us_states VALUES (?, ?, ?, ?)',
                 'order_details' : 'INSERT INTO order_details VALUES (?, ?, ?, ?, ?)'}