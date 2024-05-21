#use DOM
import time

start = time.time() #start time recording
import xml.dom.minidom
from xml.sax.xmlreader import AttributesImpl

DOMTree = xml.dom.minidom.parse("/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical 14/go_obo.xml")

collection = DOMTree.documentElement
elements = collection.getElementsByTagName('term')

cnt_mole_func = 0
cnt_bio_process = 0
cnt_cell_comp = 0

for term in elements:
    if term.getElementsByTagName('namespace')[0].firstChild.nodeValue == 'molecular_function':
        cnt_mole_func += 1
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue == 'biological_process':
        cnt_bio_process += 1
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue == 'cellular_component':
        cnt_cell_comp += 1

print('DOM:')
print('molecular_function:', cnt_mole_func)
print('biological_process:', cnt_bio_process)
print('cellular_component:', cnt_cell_comp)

end = time.time() #end time recording
print('Time(DOM API):', end-start,'seconds')

#use SAX API
start2 = time.time() #start time recording
import xml.sax
cnt_mole_func2 = 0
cnt_bio_process2 = 0
cnt_cell_comp2 = 0
class termHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.tag = ""
        self.id = ""
        self.name = ""
        self.namespace = ""

    def startElement(self,name,attributes):
        self.tag= name
        if name == "namespace":
            self.tag = "namespace"
        else:
            pass
    def characters(self, content):
        self.content = content
        if self.tag == "namespace":
            if content == "molecular_function":
                global cnt_mole_func2
                cnt_mole_func2 += 1
            elif content == "biological_process":
                global cnt_bio_process2
                cnt_bio_process2 += 1
            elif content == "cellular_component":
                global cnt_cell_comp2
                cnt_cell_comp2 += 1
            
    def EndElement(self, content):
        pass

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

Handler = termHandler()
parser.setContentHandler(Handler)
parser.parse('/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical 14/go_obo.xml')

print('SAX:')
print('molecular_function:', cnt_mole_func2)
print('biological_process:', cnt_bio_process2)
print('cellular_component:', cnt_cell_comp2)
    
end2 = time.time() #end time recording
print('Time(SAX API):', end2-start2,'seconds')
#### The time of SAX API is shorter than DOM API. SAX API is the quickest.

# ready to print graphs
import matplotlib.pyplot as plt

plt.figure(figsize=(15,6))
labels = ['molecular_function', 'biological_process', 'cellular_component']

# deal with the data from DOM and SAX methods into lists
DOM_data = [cnt_mole_func, cnt_bio_process, cnt_cell_comp]
SAX_data = [cnt_mole_func2, cnt_bio_process2, cnt_cell_comp2]

#first sub-plot
plt.subplot(1,2,1)
plt.bar(labels, DOM_data, color=['b'], width=0.5)
for a,b,i in zip(labels, DOM_data, range(len(labels))):
    plt.text(a, b+0.15, str(DOM_data[i]), ha='center', fontsize=10) #This code of line 98 & 99 was cited from https://www.csdn.net

plt.title('Distribution of GO terms(DOM)')
plt.ylabel('Frequency of GO terms')
plt.xlabel('Categories of GO terms')

# second sub-plot
plt.subplot(1,2,2)
plt.bar(labels, SAX_data, color=['r'], width=0.5)
for a,b,i in zip(labels, SAX_data, range(len(labels))):
    plt.text(a, b+0.15, str(SAX_data[i]), ha='center', fontsize=10) #This code of line 108 & 109 was cited from https://www.csdn.net

plt.title('Distribution of GO terms(SAX)')
plt.ylabel('Frequency of GO terms')
plt.xlabel('Categories of GO terms')

plt.show()
plt.clf()


# The time of SAX API is shorter than DOM API. SAX API is the quickest.