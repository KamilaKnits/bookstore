from books.models import Book   # connect parameters from books model
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num

# define a function that takes the ID 
def get_bookname_from_id(val):
    # this ID is used to retrieve the name from the record
    bookname = Book.objects.get(id=val)

    # and the name is returned back
    return bookname

def get_graph():
    # create a BytesIO buffer for the image
    buffer = BytesIO()

    # create a plot with a bytesIO object as a file like object
    # set format to png
    plt.savefig(buffer, format='png')

    # set cursor to the beginning of the stream
    buffer.seek(0)

    # retrieve the contect of the file
    image_png = buffer.getvalue()

    # encode the bytes-like objec
    graph = base64.b64encode(image_png)

    # decode to get the string as output
    graph = graph.decode('utf-8')

    # free up the memory of buffer
    buffer.close()

    # return the image/graph
    return graph



# chart_type: user input of type of chart,
# data: pandas dataframe
def get_chart(chart_type, data, **kwargs): 
    # kwargs = additional keyword arguments
    #**kwargs = collects and extra named arguments into a dictionary

    #switch plot backend to AGG - to write to file
    # preferred to write PNG files
    plt.switch_backend('AGG')

    # specify figure size
    fig = plt.figure(figsize=(6,6))

    # select chart_type based on user input from the form
    if chart_type == '#1':
        # Convert to native Python datetime if needed
        dates = [d.to_pydatetime() for d in data['date_created']]  # if using pandas Series
        x = date2num(dates)  # convert to matplotlib-friendly format

        plt.bar(x, data['quantity'], width=1)  # width can be adjusted for spacing
        plt.title('Quantity Sold')
        plt.xlabel('Date Sold')
        plt.ylabel('Quantity')

        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=45)
        
        # print(data['date_created'])
        # for d in data['date_created']:
        #     print(type(d), d)
        
    
    elif chart_type == '#2':
        #generate pie chart based on the price. 
        #The book titles are sent from the view as labels
        labels=kwargs.get('labels')
        plt.pie(data['price'], labels=labels)
        plt.title('Total Sold')

        
        # print("Labels:", labels)
    

    elif chart_type == '#3':
        #plot line chart based on date on x-axis and price on
        #y-axis

        dates = [d.to_pydatetime() for d in data['date_created']]  # if using pandas Series
        x = date2num(dates)  # convert to matplotlib-friendly format
        plt.plot(data['date_created'], data['price'])
        plt.title('Total Sold')
        plt.xlabel('Date Sold')
        plt.ylabel('Price')

        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=45)

    else:
        print('unknown chart type')

    # specify layout details
    plt.tight_layout()

    # render the graph to file
    chart = get_graph()
    return chart