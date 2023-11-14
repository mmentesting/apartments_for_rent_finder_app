from zillowmanager import ZillowData
from dataentry import DataForm

ZILLOW_URL = "https://www.zillow.com/back-bay-boston-ma/rentals/?searchQueryState=##########"
ZILLOW_HEADER = {
      "User-Agent": "##########",
      "Accept-Language": "##########",
}
FORM_URL = "https://docs.google.com/forms/##########"

zillow_data = ZillowData()
zillow_data.make_soup(ZILLOW_URL, ZILLOW_HEADER)

data_form = DataForm()
data_form.fill_forms(FORM_URL, zillow_data.addresses, zillow_data.prices, zillow_data.links)
