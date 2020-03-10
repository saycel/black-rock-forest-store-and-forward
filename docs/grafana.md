// Add red arrows to images where buttons or text is placed. 

### Grafana
Grafana is a multi-platform open source analytics and interactive visualization software. It provides charts, graphs, and alerts. Grafana is currently part of the installation package included in this repository. 

### Access Grafana
Access Grafana thorugh the IP address where you installed the Store and Forward node software.  The Black Rock Forest you can http://165.22.191.125:3000/ 

You will need a login and Password. Ask Black Rock Forest security advisor for your credentials. 


### How To Add A sensor to a Grafana Panel
Follow [Sensor Node Guide](./docs/esp8266.md) to make a ESP8266 sensor node.  
On line 133 and 141 of the firmware code you changed "YOUR-SENS" to your own name for the sensor. For this example we will give it the name "SEN-001" 

#### Step 1:
Login into Grafana

#### Step 2:
On the upper right of the page, click "Add Panel".

![GitHub Logo](./images/Grafana-Step-1.png "Add Panel")

Step 2:

A panel titled 'New Panel' will appear. Click 'Choose Visualization'.

![GitHub Logo](./images/Grafana-Step-2.png "Choose Visualization")

Step 3:

Choose 'Graph'.

![GitHub Logo](./images/Grafana-Step-3.png "Choose 'Graph'")

Step 4:

After choosing graph, you will click the three disks on the upper left of this screenshot. This is where you'll set the database query.

![GitHub Logo](./images/Grafana-Step-4.png "Click Queries")

Step 5:

In the top row, named 'From', change 'Metric column' to 'unit_string'.

![GitHub Logo](./images/Grafana-Step-5.png "Update 'From'")

Step 6:

In the third row, named 'Where', click the plus sign then click 'Expression'.

![GitHub Logo](./images/Grafana-Step-6.png "Update 'Where'")

Step 7:

In the same row, named 'Where', change the expression to match your query. In this instance we are searching a device id named 'dendro6'.

![GitHub Logo](./images/Grafana-Step-7.png "Update 'Where'")

Step 8:

Now click the settings icon on the far right. Here you can change the name of your panel.

![GitHub Logo](./images/Grafana-Step-8.png "Update panel name")

Step 9:

Finally, go back to your dashboard to see your new Panel.

![GitHub Logo](./images/Grafana-Step-9.png "View dashboard")




