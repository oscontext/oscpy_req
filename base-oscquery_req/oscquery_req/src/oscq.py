#!/usr/bin/python3
"""
Orginizaton:    Open Source Context
Author:         Donald "Mac" McCarthy
File:           oscq.py
Description:    This file is intended to serve as an ongoing base for requests
                based queries into the Open Source Context API.
Version:        0.0.2
Modify Date:    08 MAR 2022
"""

import requests
import json
import sys
import urllib.parse
import math

class oscQuery:
    def __init__(self, query, apikey, size=None, url=None, sort=None,\
            fields=None, rt=None, page=None, start=None):
        self.query = query
        self.url = url
        self.apikey = apikey
        self.size = size
        self.sort = sort
        self.fields = fields
        self.rt = rt
        self.page = page
        self.start = start

    #This will run a simple query against the domainsquery endpoint to find any
    #A or AAAA records that match the queried IP.
    def d_ip_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        page=None):
        query = "value_ip:'" + query + "'"
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, page=page)
        if my_obj.page == None:
            return oscQuery.__dquery(my_obj)
        else:
            return oscQuery.__dquery_p(my_obj)

    #This will run a simple query looking for all the hosts/subdomains belonging
    #to the queried domain. qname.right is used to ensure the user gets the
    #intended data back. If a subdomain and/or non-recognized domain is entered,
    #the user will still get any .right matching data.
    def d_dom_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        page=None):
        query = "domain:" + query
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, page=page)
        if my_obj.page == None:
            return oscQuery.__dquery(my_obj)
        else:
            return oscQuery.__dquery_p(my_obj)

    #This will run a query for a specific host name. I.e., if the user enters
    #the value example.com, the return results will be for that EXACT query. No
    #results for www.example.com will be returned. This is useful when looking
    #for a specific host.
    def d_qn_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        page=None):
        query = "qname:" + query
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, page=page)
        if my_obj.page == None:
            return oscQuery.__dquery(my_obj)
        else:
            return oscQuery.__dquery_p(my_obj)

    #This will run a query looking for records with a specific value. If the
    #value queried is an IP address, then the user will most likely get A and
    #AAAA records in return. If an email address is entered, the user will most
    #likely get an soa_email record in return.
    def d_val_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        page=None):
        query = "value:" + query
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, page=page)
        if my_obj.page == None:
            return oscQuery.__dquery(my_obj)
        else:
            return oscQuery.__dquery_p(my_obj)

    #This is for complex queries. A lucene compatible query string should be
    #provided to this function. I.e. "qname.tokens:mywish AND type:cname". The
    #full range of features and fields for the Open Source Context API will be
    #available via this function. If you need additional information, please
    #refer to the API specification document provied by you OSC representative.
    def d_luc_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        page=None):
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, page=page)
        if my_obj.page == None:
            return oscQuery.__dquery(my_obj)
        else:
            return oscQuery.__dquery_p(my_obj)

    #This is for a simple as query. This will return events where the query is
    #either in the asn or different_asn field.
    def b_as_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        rt=None, page=None):
        query = "asn:" + query + " OR different_asn:" + query
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, rt=rt, page=page)
        if my_obj.page == None:
            return oscQuery.__bquery(my_obj)
        else:
            return oscQuery.__bquery_p(my_obj)

    #This is for a simple prefix_exact query. It will return events where the
    #query is either in the prefix_exact or different_prefix_exact field.
    def b_pe_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        rt=None, page=None):
        query = "prefix_exact:'" + query + "'" + " OR different_prefix_exact:'"\
            + query + "'"
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, rt=rt, page=page)
        if my_obj.page == None:
            return oscQuery.__bquery(my_obj)
        else:
            return oscQuery.__bquery_p(my_obj)

    #This is for a simple event type query. It will return results matching the
    #the type of event searched for.
    def b_et_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        rt=None, page=None):
        query = "event_type:" + query
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, rt=rt, page=page)
        if my_obj.page == None:
            return oscQuery.__bquery(my_obj)
        else:
            return oscQuery.__bquery_p(my_obj)

    #This is for complex queries. A lucene compatible query string should be
    #provided to this function.
    #I.e. asn:<target_asn> AND first_seen:[2021-01-01 TO 2021-01-05]. The
    #full range of features and fields for the Open Source Context API will be
    #available via this function. If you need additional information, please
    #refer to the API specification document provied by you OSC representative.
    def b_luc_query(query, apikey, size=None, url=None, sort=None, fields=None,\
        rt=None, page=None):
        my_obj = oscQuery(query, apikey, size=size, url=url, sort=sort,\
            fields=fields, rt=rt, page=page)
        if my_obj.page == None:
            return oscQuery.__bquery(my_obj)
        else:
            return oscQuery.__bquery_p(my_obj)

    """
    All functions below this comment are intended to be class private functions.
    Please use the functions above this comment to interact with them.
    """

    #This function actually executest the search against the domainsquery API
    #endpoint using requests.
    def __dquery(my_obj):
        if my_obj.url == None:
            my_obj.url = 'https://api.oscontext.com/api/v2/domainsquery'
        if my_obj.size == None:
            my_obj.size = '100'
        if my_obj.sort == None:
            my_obj.sort = 'last_seen:desc'
        if my_obj.fields == None:
            my_obj.fields = 'date,last_seen,domain,qname,type,qtype,'
            my_obj.fields = my_obj.fields + 'value,value_ip'
        if my_obj.query == None:
            mye = dict()
            dict['error'] = 'User must provide a query string'
            return json.loads(mye)
        if my_obj.apikey == None:
            mye = dict()
            dict['error'] = 'User must provide a valid API key'
            return json.loads(mye)


        #The query string will be built from the given query
        #First, url encode the issued data query
        qstring = 'q=' + urllib.parse.quote(my_obj.query)
        #Add the API Key
        qstring = qstring + '&token=' + my_obj.apikey
        #Add the number of results desired
        qstring = qstring + '&size=' + str(my_obj.size)
        #Add the sort order
        qstring = qstring + '&sort=' + my_obj.sort
        #Is this part of a pafinated query?
        if my_obj.start != None:
            qstring = qstring + '&start=' + my_obj.start
        #Add the return fields desired (unless debugging)
        if my_obj.fields != 'debug':
            qstring = qstring + '&fields=' + my_obj.fields

        payload = ''
        headers = {
            'content-type': 'application/x-www-form-urlencoded',\
            'referer': 'osc_integration_libs',\
            'Accept-Encoding': 'br, gzip, compress'\
        }
        try:
            resp = requests.get(my_obj.url, data=payload,\
                headers=headers, params=qstring, timeout=120)
        except Exception as e:
            jsonResp = dict()
            jsonResp['error'] = str(e)
            return jsonResp
        try:
            jsonResp = resp.json()
        except Exception as e:
            jsonResp = dict()
            jsonResp['json_err'] = str(e)
            jsonResp['ret_data'] = str(b)
            return jsonResp

        return jsonResp

    def __bquery(my_obj):
        if my_obj.url == None:
            my_obj.url = 'https://api.oscontext.com/api/v2/bgpevents'
        if my_obj.size == None:
            my_obj.size = '100'
        if my_obj.sort == None:
            my_obj.sort = 'last_seen:desc'
        if my_obj.query == None:
            mye = dict()
            dict['error'] = 'User must provide a query string'
            return json.loads(mye)
        if my_obj.apikey == None:
            mye = dict()
            dict['error'] = 'User myst provide a valid API key'
            return json.loads(mye)
        """
        There are a lot more fields for BGP than for DNS,
        rt (return type) is a way of specifying a few different default optput
        fields.

        sml
        --------
        The small option will bring back a minimal number of fields:
            first_seen, last_seen, asn, prefix_exact, event_type, different_asn,
            different_prefix_exact

        med
        --------
        The medium option will bring back all the information in the small
        option as well as the following fields:
            as_path, different_as_path, prefix, different_prefix

        lrg
        --------
        The large option will bring back all the fields in the medium options as
        well as the following fields:
            as_path_list - the as_path field in a common list format
            different_as_path_list - different_as_path field in a common list
                format
            different_first_seen, different_last_seen

        mnl
        --------
        The manual option will bring back only the specified fields in the
        fields argument of the object.

        dbg
        --------
        The debug option will bring back all fields
        """

        f = ['first_seen','last_seen','asn','prefix_exact','event_type',\
            'different_asn','different_prefix_exact','as_path',\
            'different_as_path','prefix','different_prefix','as_path_list'\
            'different_as_path_list','different_first_seen',\
            'different_last_seen']
        fields=''
        if my_obj.rt == 'med':
            for i in range (0,10):
                fields = fields + f[i] + ','
            fields = fields.rstrip(',')
        elif my_obj.rt == 'lrg':
            for i in range (0,14):
                fields = fields + f[i] + ','
            fields = fields.rstrip(',')
        elif my_obj.rt == 'mnl':
            fields = my_obj.fields
        elif my_obj.rt == 'dbg':
            pass
        else:
            for i in range (0,6):
                fields = fields + f[i] + ','
            fields = fields.rstrip(',')


        #The query string will be built from the given query
        #First, url encode the issued data query
        qstring = 'q=' + urllib.parse.quote(my_obj.query)
        #Add the API Key
        qstring = qstring + '&token=' + my_obj.apikey
        #Add the number of results desired
        qstring = qstring + '&size=' + str(my_obj.size)
        #Add the sort order
        qstring = qstring +'&sort=' + my_obj.sort
        #Add the return fields desired
        if my_obj.rt != 'dbg':
            qstring = qstring + '&fields=' + fields

        payload = ''
        headers = {
            'content-type': 'application/x-www-form-urlencoded',\
            'referer': 'osc_integration_libs',\
            'Accept-Encoding': 'br, gzip, compress'\
        }
        try:
            resp = requests.get(my_obj.url, data=payload,\
                headers=headers, params=qstring, timeout=120)
        except Exception as e:
            jsonResp = dict()
            jsonResp['error'] = str(e)
            return jsonResp
        try:
            jsonResp = resp.json()
        except Exception as e:
            jsonResp = dict()
            jsonResp['json_err'] = str(e)
            jsonResp['ret_data'] = str(b)
            return jsonResp

        return jsonResp

    #This function actually executes the search against the domainsquery API
    #endpoint using requests. It includes the necessary logic to paginate using
    #**MULTIPLE** queries to retreive up to 2,000,000. Please note this will
    #use **MULTIPLE** queries if there are more than 100,000 results meeting
    #your search criteria.
    def __dquery_p(my_obj):
        my_obj.size = '100000'

        #First we need to determine how many results meet the criteria. This
        #will determine if we need multiple queries, and if so how many.
        #Regardless of how many matching results there are, it will return a
        #maximum of 2,000,000.
        init_res = oscQuery.__dquery(my_obj)
        if int(init_res['total']) >= 100001:
            lc = 100000
            t_lines = init_res['total']
            if t_lines > 2000000:
                t_lines = 2000000
            qc = math.ceil(((t_lines-100000)/100000))
            info = str("{:,}".format(init_res['total'])) + ' results found.' +\
            ' Returning ' + str(t_lines) + '.'
            total = str(init_res['total'])
        else:
            return init_res

        res_list = list()
        for i in init_res['results']:
            res_list.append(i)

        while qc > 0:
            my_obj.start = str(lc)
            init_res = oscQuery.__dquery(my_obj)
            for i in init_res['results']:
                res_list.append(i)
            lc = lc + 100000
            qc = qc - 1

        res_dict = dict()
        res_dict['info'] = info
        res_dict['total'] = init_res['total']
        res_dict['returning'] = t_lines
        res_dict['results'] = res_list

        return res_dict

    #This function actually executes the search against the bgpevents API
    #endpoint using requests. It includes the necessary logic to paginate using
    #**MULTIPLE** queries to retreive up to 2,000,000. Please note this will
    #use **MULTIPLE** queries if there are more than 100,000 results meeting
    #your search criteria.
    def __bquery_p(my_obj):
        my_obj.size = '100000'

        #First we need to determine how many results meet the criteria. This
        #will determine if we need multiple queries, and if so how many.
        #Regardless of how many matching results there are, it will return a
        #maximum of 2,000,000.
        init_res = oscQuery.__bquery(my_obj)
        if int(init_res['total']) >= 100001:
            lc = 100000
            t_lines = init_res['total']
            if t_lines > 2000000:
                t_lines = 2000000
            qc = math.ceil(((t_lines-100000)/100000))
            info = str("{:,}".format(init_res['total'])) + ' results found.' +\
            ' Returning ' + str(t_lines) + '.'
            total = str(init_res['total'])
        else:
            return init_res

        res_list = list()
        for i in init_res['results']:
            res_list.append(i)

        while qc > 0:
            my_obj.start = str(lc)
            init_res = oscQuery.__bquery(my_obj)
            for i in init_res['results']:
                res_list.append(i)
            lc = lc + 100000
            qc = qc - 1

        res_dict = dict()
        res_dict['info'] = info
        res_dict['total'] = init_res['total']
        res_dict['returning'] = t_lines
        res_dict['results'] = res_list

        return res_dict
