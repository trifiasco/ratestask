# Project Setup
- clone this repository
- rename the `.env.dev.sample` to `.env.dev`
- run `docker-compose up --build`, this should start the project
- to run the tests - `docker-compose exec web pytest`

# Usage
- `curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"`

# Data Defination

## Ports

Information about ports, including:

* 5-character port code
* Port name
* Slug describing which region the port belongs to

## Regions

A hierarchy of regions, including:

* Slug - a machine-readable form of the region name
* The name of the region
* Slug describing which parent region the region belongs to

Note that a region can have both ports and regions as children, and the region
tree does not have a fixed depth.

## Prices

Individual daily prices between ports, in USD.

* 5-character origin port code
* 5-character destination port code
* The day for which the price is valid
* The price in USD

