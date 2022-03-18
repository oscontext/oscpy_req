![alt text](https://blog.oscontext.io/content/images/2021/01/img2-1800-1200-1.jpg)
# Open Source Context Python Library (Requests)

### This project provides users with a common code base to use when interacting with the Open Source Context API using Python and requests

In order to use this library users will need the following:

* An API key for the Open Source Conetext API. More information available at https://oscontext.com
* Installed, working Python3 installation
* Installed, working python requests library
* A copy of the API specification provided by your Open Source Context representative (for reference).

This library is primarily developed and maintained on linux (Ubuntu and Fedora) and Apple MacOS (Big Sur and Monterey) systems. Limited testing is done on Windows based systems.

Query results format:

JSON:

* Info: Information about how many results were found and returned (`type:<string>`)
* Total: Number of results returned. (`type:<int>`)
* Results: List of resutls returned. (`type:<list>` of `type:<dict>`)

## PassiveDNS Functionality
There are four "simple" methods for querying pDNS in this library:

* `d_ip_query`
* `d_dom_query`
* `d_qn_query`
* `d_val_query`

There is also a method for complex queries as well:

* `d_luc_query`

Each one will be described here with some basic examples.

### d\_ip\_query
This method allows for the simple querying of an IP address or CIDR range.

* query (required) - This should be the IP address or CIDR range being queried. (I.e. '192.168.0.1' or '192.168.0.0/24')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. By default all fields other than the `_key` field are returned.
* page (optional) - This is the option for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.d_ip_query('192.168.2.100',<api_key>,size=50)`
* `oscQuery.d_ip_query('192.168.0.0/16',<api_key>,page=True)`
* `oscQuery.d_ip_query('10.10.10.10',<api_key>,size=5,fields='date,last_seen,qname')`

### d\_dom\_query
This method allows for the simple querying of all hosts/subdomains for a single domain.

* query (required) - This should be the name of the domain you would like to query. I.e `'example.com'` or `'mydomain.tld'`
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. By default all fields other than the `_key` field are returned.
* page (optional) - This is the option for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.d_dom_query('example.com',<api_key>,size=50)`
* `oscQuery.d_dom_query('largedomain.tld',<api_key>,page=True)`
* `oscQuery.d_dom_query('mydomain.tld',<api_key>,size=5,fields='date,last_seen,qname')`


### d\_qn\_query
This method allows for the simple querying of a specific hostname.

* query (required) - This should be the name of the host you would like to query. I.e `'www.example.com'` or `'mail.example.com'`
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. By default all fields other than the `_key` field are returned.
* page (optional) - This is the option for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.d_qn_query('mx1.example.com',<api_key>,size=50)`
* `oscQuery.d_qn_query('loadbal.mydomain.tld',<api_key>,page=True)`
* `oscQuery.d_qn_query('webapp.example.com',<api_key>,size=5,fields='date,last_seen,qname')`

### d\_val\_query
This method allows for the simple querying of records which have a specific value. This could be used to find CNAME redirects, SPF records, domains on a particular nameserver, etc...

* query (required) - This should be the name of the value you would like to query. I.e `'www.example.com.cdn.redirect.tld'` or `'ns1.mydomain.tld'`
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. By default all fields other than the `_key` field are returned.
* page (optional) - This is the option for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.d_val_query('v=spf1 a mx mx:mail.example.com',<api_key>,size=50)`
* `oscQuery.d_val_query('ns2.mydomain.tld',<api_key>,page=True)`
* `oscQuery.d_val_query('www.example.com.cdn.redirect.tld',<api_key>,size=5,fields='date,last_seen,type')`

### d\_luc\_query
This method allows for complex querying of the domainsquery endpoint using lucene syntax. More information on lucene syntax can be found at http://www.lucenetutorial.com/lucene-query-syntax.html

* query (required) - This should be the name of the value you would like to query. I.e `'domain:example.com AND last_seen:[2022-01-01 TO 2022-01-13]'` or `'qname.right:mydomain.tld AND (type:mx OR type:txt)'`
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. By default all fields other than the `_key` field are returned.
* page (optional) - This is the option for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.d_luc_query('type:soa_server AND value:/ns[1-2]\.example\.com/',<api_key>,size=50)`
* `oscQuery.d_luc_query('last_seen:2022-01-01 AND qname.tokens:example',<api_key>,page=True)`
* `oscQuery.d_luc_query('type:cname AND qname.right:mydomain.tld',<api_key>,size=5,fields='date,last_seen,qname')`

## PassiveBGP Functionality
There are three "simple" methods for querying pDNS in this library:

* `b_as_query`
* `b_pe_query`
* `b_et_query`

There is also a method for complex queries as well:

* `b_luc_query`

Each one will be described here with some basic examples.

There are also multiple types of output which can be specified:

* sml (small) - The small option will bring back a minimal number of fields:
	* `first_seen`
	* `last_seen`
	* `asn`
	* `prefix_exact`
	* `event_type`
	* `different_asn`
	* `different_prefix_exact`
* med (medium) - The medium option will bring back all the information in the small option as well as the following fields:
	* `as_path`
	* `different_as_path`
	* `prefix`
	* `different_prefix`
* lrg (large) - The large option will bring back all the fields in the medium options as well as the following fields:
	* `as_path_list` - the `as_path` field in a common list format
	* `different_as_path_list` - `different_as_path` field in a common list format
	* `different_first_seen`
	* `different_last_seen`
* mnl (manual) - The manual option will bring back only the specified fields in the ields argument of the object.
* dbg (debug) - The debug option will bring back all fields

If no return type option is specified, the default is small.

### b\_as\_query
This method allows for the simple querying of a specific ASN.

* query (required) - This should be the ASN being queried. (I.e. '12354')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. This field should only be used if specifying the `mnl` (manual) return type.
* rt (optional) - This is where the user can specify the output type they want returned. This includes the `sml`, `med`, `lrg`, `mnl`, or `dbg` types. If specifying `mnl`, make sure you provide the listed fields in the `fields` option.
* page (optional) - This is the optoin for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.b_as_query('12345',<api_key>,size=50)`
* `oscQuery.b_as_query('12345',<api_key>,page=True,rt='med')`
* `oscQuery.b_as_query('12345,<api_key>,size=5,fields='first_seen,last_seen',fields='mnl')`

### b\_pe\_query
This method allows for the simple querying of a specific prefix announcement.

* query (required) - This should be the prefix being queried. (I.e. '1.2.0.0/16' or '1.2.3.0/24')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. This field should only be used if specifying the `mnl` (manual) return type.
* rt (optional) - This is where the user can specify the output type they want returned. This includes the `sml`, `med`, `lrg`, `mnl`, or `dbg` types. If specifying `mnl`, make sure you provide the listed fields in the `fields` option.
* page (optional) - This is the optoin for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.b_pe_query('1.2.0.0/16',<api_key>,size=50)`
* `oscQuery.b_pe_query('1.2.3.0/24',<api_key>,page=True,rt='med')`
* `oscQuery.b_pe_query('1.2.5.0/24',<api_key>,size=5,fields='first_seen,last_seen',fields='mnl')`

### b\_et\_query
This method allows for the simple querying of a specific BGP event type.

* query (required) - This should be the event type being queried. (I.e. 'bgp-new-prefix' or 'bgp-withdrawn-prefix')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. This field should only be used if specifying the `mnl` (manual) return type.
* rt (optional) - This is where the user can specify the output type they want returned. This includes the `sml`, `med`, `lrg`, `mnl`, or `dbg` types. If specifying `mnl`, make sure you provide the listed fields in the `fields` option.
* page (optional) - This is the optoin for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.b_et_query('bgp-new-prefix',<api_key>,size=50)`
* `oscQuery.b_et_query('bgp-withdrawn-prefix',<api_key>,page=True,rt='med')`
* `oscQuery.b_et_query('bgp-different-origin',<api_key>,size=5,fields='first_seen,last_seen',fields='mnl')`

### b\_luc\_query
This method allows for the complex querying of the bgpevents endpoint using lucene syntax. More information on lucene syntax can be found at http://www.lucenetutorial.com/lucene-query-syntax.html

* query (required) - This should be the event type being queried. (I.e. 'asn:12345 AND first_seen:2022-01-01' or 'asn:12345 AND event_type:bgp-different-origin')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - The base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint. If you have any questions about this field, please contact your Open Source Context representative or support.tech@oscontext.com.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields they want returned in the results. This field should only be used if specifying the `mnl` (manual) return type.
* rt (optional) - This is where the user can specify the output type they want returned. This includes the `sml`, `med`, `lrg`, `mnl`, or `dbg` types. If specifying `mnl`, make sure you provide the listed fields in the `fields` option.
* page (optional) - This is the optoin for a paginated query when results are over 100,000. Using this option will cause several things to happen:
	* The size of the results set will automatically be overridden to 100,000, regardless of what the user selects.
	* If there are more than 100,000 results, **MULTIPLE** queries will be run.
	* A maximum of 20 queries will be run which will return up to a total of 2 million results. This is not user controllable in this version.

Examples:

* `oscQuery.b_et_query('asn:12345 AND event_type:bgp-withdrawn-prefix',<api_key>,size=50)`
* `oscQuery.b_et_query('asn:12345 AND last_seen:2022-02-01',<api_key>,page=True,rt='med')`
* `oscQuery.b_et_query('asn:12345 AND different_asn:23456',<api_key>,size=5,fields='first_seen,last_seen',fields='mnl')`

## Notes:
This is not intended to be an exhaustive guide to searching the OSC API. If you need more assistance, please contact support.tech@oscontext.com and someone will be glad to assist you.

Open Source Context offers training to almost any orginization (not just customers) on how to improve security operations through the use of increased knowledge, open source tooling, automation, passiveDNS and passiveBGP. Although the training is given using the OSC API and tooling, the concepts taught are applicable across any reliable pDNS or pBGP data set.

### TO DO:
OSC indends to maintain and improve this library. Things on the roadmap are:

* Allow user to specify maximum number of queries and/or results in pagniated queries.
* Select CSV, TSV, LDJSON, or table formated results
