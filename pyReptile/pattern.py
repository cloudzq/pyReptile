from bs4 import BeautifulSoup

# Define data cleaning classes
class DataPattern(object):
    def get_data(self, response, selector, **kwargs):
        parser = kwargs.get('parser', 'html.parser')
        tempList = []
        soup = BeautifulSoup(response, parser)
        temp = soup.select(selector=selector)
        for i in temp:
            tempList.append(i.getText())
        return tempList


dataPattern = DataPattern()
