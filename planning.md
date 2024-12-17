# Planning

## Concept Ladder

Up is why, down is how

| Because uber wants to make money, public transport requires raising taxes, and the colleges haven't faced enough pressure to make it affordable |
| Because surge pricing, no public transport, and no good shuttles from the colleges |
| Because getting to the airport is a lot more expensive than it needs to be |
| Claremont Rideshare |
| Make an app that automatically pairs groups of students leaving from the same place at the same time so they can share ubers |
| Make an opensource webapp that's pretty barebones but easy to use- connected to the uber and lyft apis, and validated with claremont id |
| Figure out basic construction of website, build pre-beta that has places to plug in all the apis and authentication, reach out to TCCS, uber, and lyft- release |

## Project Roadmap

1. Basic webapp construction
    1. get flask working
    2. build a login system
    3. make user input system- time, place, date
    4. make hash table for matching
2. integration
    1. figure out how uber and lyft apis work
    2. make scheduling integration
    3. make payment integration
3. payment
    1. figure out whether to do it through uber/lyft or separately
    2. implement it
4. partnership
    1. reach out to uber, lyft, tccs
    2. start thinking about deployment
