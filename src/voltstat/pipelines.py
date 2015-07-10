from scrapy.exceptions import DropItem
import urlparse
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class voltstatPipeline(object):
    
    def process_item(self, item, spider):
        if item['data']:
            data_lists = item['data'][0]
            data_lists = data_lists.split('\n')[2]
            data_lists = data_lists.replace('Sacknet.MileageGraph.SetupMileageGraph(','').replace(');','').replace('\r','')
            dataseries1 = data_lists.split(', ')[2].replace('[[',' ').replace(']]',' ').split('],[')
            dataseries2 = data_lists.split(', ')[3].replace('[[',' ').replace(']]',' ').split('],[')
            length_series = len(dataseries1) 
            print length_series
            print dataseries1[0].split(',')[0]
            print dataseries2[1].split(',')[0]
            combined_list = [] 
            for  i in  range(0, length_series - 1):
                dataset1 = dataseries1[i].split(',')
                dataset2 = dataseries2[i].split(',')
                date1 = dataset1[0].replace("'",'').split('/')
                date2 = dataset2[0].replace("'",'').split('/')
                newdate1 = date1[1] + "." + date1[0] + "." +  date1[2]
                newdate2 = date2[1] + "." + date2[0] + "." +  date2[2]
                combined_list.append(newdate1 + ", " + dataset1[1] + ", " +  newdate2 + ", " +  dataset2[1])
             
            item['data'] = combined_list
            item['metadata'] = length_series
            return item

#===============================================================================
#         if item['data1']:
#             item_string= item['data1'][0].replace('\n','').replace('\r','').replace('\t','').replace(', true);});','').replace("$(function() {Sacknet.MileageGraph.SetupMileageGraph('/Stats/UpdateMileageGraph/1', null,",'').replace("$(function(){Sacknet.MileageGraph.SetupMileageGraph('/Stats/UpdateMileageGraph/1', null,",'') 
#             item_list = item_string.split("]], [[")
# #        print_string = string_item.index['[['] Stats.$(function(){Sacknet.MileageGraph.SetupMileageGraph(.UpdateMileageGraph, null,
#             dataseries1 = item_list[0].replace('[[','').replace(' ','').replace("'","").split('],[')
#             dataseries2 = item_list[1].replace(']]','').replace(' ','').replace("'","").split('],[')
#             length_series = len(dataseries1) 
#             print dataseries1[0].split(',')[0]
#             print dataseries1[1].split(',')[0]
#             pause
#             combined_list = []
#             # print dataseries1[0].split(',')[0]
#             #===================================================================
#             # combined_list.append(dataseries1[0].split(',')[0] + ", " + dataseries1[0].split(',')[1] + ", " +  dataseries2[0].split(',')[0] + ", " +  dataseries2[0].split(',')[1])
#             # combined_list.append(dataseries1[1].split(',')[0] + ", " + dataseries1[1].split(',')[1] + ", " +  dataseries2[1].split(',')[0] + ", " +  dataseries2[1].split(',')[1])
#             #===================================================================
# 
#             for  i in  range(0, length_series - 1):
#                 date1 = dataseries1[i].split(',')[0].split('/')[1] + "." + dataseries1[i].split(',')[0].split('/')[0] + "." +  dataseries1[i].split(',')[0].split('/')[2]
#                 date2 = dataseries2[i].split(',')[0].split('/')[1] + "." + dataseries2[i].split(',')[0].split('/')[0] + "." +  dataseries2[i].split(',')[0].split('/')[2]
#                 combined_list.append(date1 + ", " + dataseries1[i].split(',')[1] + ", " +  date2 + ", " +  dataseries2[i].split(',')[1])
#             
#             item['data1'] = combined_list
#             item['metadata'] = length_series
#             return item
#===============================================================================
        
    #===========================================================================
    #     if item['linkwithprice']:
    #         parsed = urlparse.urlparse(item['linkwithprice'][0])
    #         item['price'] = urlparse.parse_qs(parsed.query)['price']
    #         item['categoryId'] = urlparse.parse_qs(parsed.query)['categoryId']  
    #         item['productid'] = urlparse.parse_qs(parsed.query)['productid']    
    #         item['sid'] = urlparse.parse_qs(parsed.query)['sid']
    #         if item['desc']:
    #             item['desc']  = item['desc'][0].replace('\n',' ')
    #         title_str = item['title'][0]
    #         if title_str.count("kaufen") > 0:
    #             item['title'] =  title_str[:title_str.index(" kaufen")]
    #         if  title_str.count("bestellen") > 0:
    #             item['title'] =  title_str[:title_str.index(" bestellen")]
    #         if title_str.count("versand") > 0:
    #             item['title'] =  title_str[:title_str.index(" versand")]
    #             
    #         #item['title'] =  title_str[:title_str.index("kaufen")]
    #         
    #         return item
    #     else:
    #         raise DropItem("Leer")
    #===========================================================================