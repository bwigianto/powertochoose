# Power to choose

The deregulated energy industry in Texas means that most residents must
choose which company they want to buy their electricity from. 
Luckily for customers, the Public Utility Commission of Texas has created 
a [website](http://www.powertochoose.org/) to help shop for electricity 
plans. You supply the zip code and the TDU (transmission and
distribution utility) and you are presented with different plans from
different retailers you can purchase. You can then sort your results by
price per kWh (for different tiers of usage), which is what most people do. 
Retailers know this and have basically gamed this website to try to get to 
the top. They accomplish this by having comically complicated pricing
plans so that the average price per kWh comes out as low as possible.
This makes it impossible to compare plans without going through and
reading individual 'Fact Sheets' and accurately estimating your own
electricity usage patterns during the period.

This repo is an attempt at making this shopping process easier. The
goal is that given an estimate of your usage during a 12-month period
you'll get back the lowest cost plan to choose.

## Getting Started

If you're not already familiar with the electricity shopping process, take
a look at [Power to Choose](http://www.powertochoose.org/) and put in
77002 for the zip code. Sort by price/kWh ascending and crack open one
of the 'Fact Sheets'. Try to understand how the pricing works. Many plans
have some combination of pricing bands, retailer base charges, delivery 
base and per kWh charges, etc. Some plans even have credits based on usage.
Pay no attention to the 'Average Price per kWh' table, that is simply 
there to confuse consumers and game the website. Those numbers are poor 
estimates of what your actual bills will be.

### Usage

For now, it is just a single python script for the plans I added in my area.

```bash
python houston.py
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

