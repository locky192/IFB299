-- INSERT PLACES OF INTEREST INFO INTO DATABASE --

-- HOTELS

insert into CityApp_cityinfo (name, 
							  landmark_type, 
                              user_type, 
                              industry_type, 
                              phone_number, 
                              unit_number, 
                              street_number, 
                              suburb, 
                              state, 
                              postcode,
                              email,
                              latitude, 
                              street_name,
                              longitude) 
                              values (
'ibis Styles Brisbane Elizabeth Street','Hotel','Tourist','Tourist','07 3337 9000','40','40','Brisbane City','QLD','4000','business@gmail.com','-27.4713676','Elizabeth St','153.0245203'),
('Pullman Brisbane King George Square','Hotel','Tourist','Tourist','(07) 3229 9111','1','1','Brisbane City','QLD','4000','business@gmail.com','-27.4683174','Ann St','153.0235326'),
('The Point Brisbane','Hotel','Tourist','Tourist','(07) 3240 0888','21','21',' Kangaroo Point','QLD','4169','business@gmail.com','-27.4740138','Lambert St','153.0364606'),
('Best Western Astor Metropole Hotel & Apartments','Hotel','Tourist','Tourist','(07) 3144 4000','193','193','Brisbane City','QLD','business@gmail.com','4000','-27.4649216','Wickham Terrace','153.0240115'),
('ibis Brisbane','Hotel','Tourist','Tourist','(07) 3237 2333','27','27','Brisbane City','QLD','4000','-27.4691718','Turbot St','business@gmail.com','153.0210804'),
('Holiday Inn Express Brisbane Central','Hotel','Tourist','Tourist','(07) 3833 8888','168','168','Spring Hill','QLD','4000','business@gmail.com','-27.4627757','Wharf Street','153.0270969'),
('The Great Southern Hotel Brisbane','Hotel','Tourist','Tourist','(07) 3221 6044','103','103','Brisbane City','QLD','4000','business@gmail.com','-27.4727829','George St','153.02569'),
('Hotel Grand Chancellor Brisbane','Hotel','Tourist','Tourist','(07) 3831 4055','23','23','Brisbane City','QLD','4000','business@gmail.com','-27.4624363','Leichhardt St','153.0217714'),
('George Williams Hotel','Hotel','Tourist','Tourist','(07) 3308 0700','317','317','Brisbane City','QLD','4000','business@gmail.com','-27.468803','George St','153.0217947'),
('Adina Apartment Hotel Brisbane Anzac Square','Hotel','Tourist','Tourist','(07) 3001 9888','255','255','Brisbane City','QLD','4000','business@gmail.com','-27.4668244','Ann St','153.026049'),
('The Sebel','Hotel','Tourist','Tourist','(07) 3224 3500','1','1','Brisbane City','QLD','4000','business@gmail.com','-27.471181','Albert St','153.0267409'),
('Hilton Brisbane','Hotel','Tourist','Tourist','(07) 3234 2000','190','190','Brisbane City','QLD','4000','business@gmail.com','-27.4691949','Elizabeth St','153.0268297'),
('Four Points by Sheraton Brisbane','Hotel','Tourist','Tourist','(07) 3164 4000','99','99','Brisbane City','QLD','4000','business@gmail.com','-27.471837','Mary St','153.0281413'),
('Novotel Brisbane','Hotel','Tourist','Tourist','(07) 3309 3309','200','200','Brisbane City','QLD','4000','business@gmail.com','-27.4635947','Creek St','153.0267066');

-- COLLEGES

insert into CityApp_cityinfo (name, 
							  landmark_type, 
                              user_type, 
                              industry_type, 
                              phone_number, 
                              unit_number, 
                              street_number, 
                              suburb, 
                              state, 
                              postcode,
                              email,
                              latitude, 
                              street_name,
                              longitude) 
                              values (
'Institute for Molecular Bioscience','College','Student','Student','(07) 3346 2180','306','306','Brisbane City','QLD','4000','business@gmail.com','-27.4981682','Carmody Rd','153.0102956'),
('James Cook University, Brisbane Campus','College','Student','Student','(07) 3001 7800','349','349','Brisbane City','QLD','4000','business@gmail.com','-27.4666898','Queen St','153.0294776'),
('UQ Business School Executive Education','College','Student','Student','(07) 3346 7111','345','345','Brisbane City','QLD','4000','business@gmail.com','-27.467049','Queen St','153.0290556'),
('CQUniversity','College','Student','Student','(07) 3295 1188','160','160','Brisbane City','QLD','4000','business@gmail.com','-27.4673899','Ann St','153.024274'),
('Queensland University of Technology','College','Student','Student','(07) 3138 2000','2','2','Brisbane City','QLD','4000','business@gmail.com','-27.4773565','George St','153.0284154'),
('University of Queensland','College','Student','Student','(07) 3365 1111','1','1','St Lucia','QLD','4072','business@gmail.com','-27.4978543','St','153.0132861'),
('Australian Institute for Bioengineering and Nanotechnology','College','Student','Student','(07) 3346 3877','75','75','Brisbane City','QLD','4072','business@gmail.com','-27.50079','Cooper Rd','153.0129083'),
('Charles Sturt University Study Centres, Brisbane','College','Student','Student','(07) 3164 4810','119','119','Brisbane City','QLD','4000','business@gmail.com','-27.4709768','Charlotte St','153.0274623'),
('UQ School of Dentistry','College','Student','Student','(07) 3365 8019','288','288','Herston','QLD','4006','business@gmail.com','-27.4489226','Herston Rd','153.0240593'),
('Torrens University Brisbane, Fortitude Valley Campus','College','Student','Student','1300 575 803','90','90','Fortitude Valley','QLD','4006','business@gmail.com','-27.4611763','Bowen Terrace','153.0360738'),
('Griffith University','College','Student','Student','(07) 3735 7111','170','170','Nathan','QLD','4111','business@gmail.com','-27.5569495',' Kessels Rd','153.0534449');

-- LIBRARIES

insert into CityApp_cityinfo (name, 
							  landmark_type, 
                              user_type, 
                              industry_type, 
                              phone_number, 
                              unit_number, 
                              street_number, 
                              suburb, 
                              state, 
                              postcode,
                              email,
                              latitude, 
                              street_name,
                              longitude) 
                              values (
'Brisbane City Council Library','Library','Student','Student','(07) 3403 8888','1','1','Fairfield','QLD','4103','business@gmail.com','-27.509139','Fairfield Road','153.0260141'),
('Brisbane City Council - Annerley Library','Library','Student','Student','(07) 3403 1735','450','450','Annerly','QLD','4103','business@gmail.com','-27.5094244','Ipswich Rd','153.0333848'),
('UQ/Mater McAuley Library','Library','Student','Student','(07) 3163 1689','1','1','South Brisbane','QLD','4101','business@gmail.com','-27.4851552','St','153.0279675'),
('Corinda Library','Library','Student','Student','(07) 3407 7701','641','641','Brisbane','QLD','4075','business@gmail.com','-27.5388809','Oxely Rd','152.9814197'),
('State Library of Queensland','Library','Student','Student','(07) 3840 7666','1','1','South Brisbane','QLD','4101','business@gmail.com','-27.4713494','Stanley PI','153.0170034');

-- MALLS

insert into CityApp_cityinfo (name, 
							  landmark_type, 
                              user_type, 
                              industry_type, 
                              phone_number, 
                              unit_number, 
                              street_number, 
                              suburb, 
                              state, 
                              postcode,
                              email,
                              latitude, 
                              street_name,
                              longitude) 
                              values (
'Indooroopilly Shopping Centre','Mall','Tourist','Tourist','(07) 3378 4022','322','322','Indooroopilly','QLD','4068','business@gmail.com','-27.4991637','Moggill Rd','152.9726834'),
('The Myer Centre, Brisbane','Mall','Tourist','Tourist','(07) 3223 6900','91','91','Brisbane City','QLD','4000','business@gmail.com','-27.4704791','Queen St','153.0247888'),
('Queen Street Mall','Mall','Tourist','Tourist','(07) 3006 6290','1','1','Brisbane City','QLD','4000','business@gmail.com','-27.4695872','Queen St','153.0252547'),
('Wintergarden','Mall','Tourist','Tourist','(07) 3229 9755','171','171','Brisbane City','QLD','4000','business@gmail.com','-27.4688187','Queen St','153.0261841'),
('MacArthur Central','Mall','Tourist','Tourist','(07) 3007 2300','255','255','Brisbane City','QLD','4000','business@gmail.com','-27.468193','Queen St','153.027771');


-- INDUSTRY

insert into CityApp_cityinfo (name, 
							  landmark_type, 
                              user_type, 
                              industry_type, 
                              phone_number, 
                              unit_number, 
                              street_number, 
                              suburb, 
                              state, 
                              postcode,
                              email,
                              latitude, 
                              street_name,
                              longitude) 
                              values (
'Brisbane Industrial Agencies','Industry','Business','Business','(07) 3351 6000','1154','1154','Arana Hills','QLD','4054','business@gmail.com','-27.3884775','Pine Rd','152.9592675'),
('All Cool Industries','Industry','Business','Business','(07) 3289 3005','239','239','Brisbane City','QLD','4000','business@gmail.com','-27.470153','George St','153.0233498'),
('Bidfood Fresh','Industry','Business','Business','(07) 3278 4538','9','9','Rocklea','QLD','4106','business@gmail.com','-27.5338448','Sherwood Road','153.0000866'),
('Hastings Deering Group Administration','Industry','Business','Business','13 12 28','973','973','Brisbane City','QLD','4105','business@gmail.com','-27.5379698','Fairfield Rd','153.0102894'),
('Simon George & Sons','Industry','Business','Business','(07) 3379 7700','1','1','Rocklea','QLD','4106','business@gmail.com','-27.5338433','Sherwood Road','153.0001473');



 