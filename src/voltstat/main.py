import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'voltstat'])
    
    #,'-o output/output.csv'

if  __name__ =='__main__':
    main()