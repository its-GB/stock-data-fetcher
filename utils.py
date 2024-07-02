from datetime import datetime, timedelta

def get_companies(config):
    companies = []
    for company_info in config.get('common', 'companies').strip().split('\n'):
        company_name, symbol = company_info.split(',')
        companies.append((company_name.strip(), symbol.strip()))
    return companies

def get_yesterday():
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')