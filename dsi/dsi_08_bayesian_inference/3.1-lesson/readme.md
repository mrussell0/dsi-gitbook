---
title: API Review with Foursquare API
type:  lesson
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  API Review with Foursquare API
Week 8 | 3.1


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

- Describe HTTPS and define an API
- Introduce the Foursquare API
- Discuss Foursquare API Functions
- Receive and iterate through data from the Foursquare API
- Describe how JSON stores data

### STUDENT PRE-WORK
*Before this lesson, students will need to be able to:*

- Review API environment and access
- Use python data structures
- Simple Exploratory Data Analysis

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| Timing | Type | Topic |
| --- | --- | --- |
| 5 min | [Opening](#opening) | A Brief Review of APIs |
| 10 min | [Introduction](#introduction) | Introduction to the Foursquare API and Python |
| 15 min | [Demo](#demo) | Looking through datatypes in Foursquare |
| 25 min | [Guided Practice](#Guided)  | Summarizing Foursquare data in Python |
| 25 min | [Independent Practice](#Indy) | Data Analysis with Foursquare API |
| 5 min |  [Conclusion](#conclusion)| Concluding Remarks |

---


#### Opening (5 min):
<a name = "opening"></a>
## (Re)Introducing APIs with Foursquare in mind

As a review, an API call is just making HTTP requests to a server and sending/receiving structured data from that endpoint. We are still communicating with URLs, however instead of receiving markup, like we do with HTML pages, we receive data. If that data is structured as JSON, we can easily start reacting and communicating with it thanks to the provided JSON methods.


#### APIs: A Quick Review (10 min):

<a name = "introduction"></a>

**Quick Check:** How do clients relate to servers?

Because our pages will be fully or partially rendered on the client side after we receive this data, there are a few best scenarios we need to take into account:

  - Certain APIs require authentication, and we need to provide an API key either as a request parameter, in the header, or in the body of the call.
  - When we make an API call after a user action, we need to give the user feedback that something is happening.
  - We update our view(s) only after we get a return from the server.
  - We need to account for us not receiving data back due to different interruptions/causes:
    - Server timeout
    - Wrong authentication information
    - User loses connection
    - Request URL not found
- [Representational state transfer (REST)](https://en.wikipedia.org/wiki/Representational_state_transfer) is the most common architecture style for passing information to and from these API endpoints.

**Quick Check:** With the person next to you, open the REST link above and in your own words, come up with a description of REST.

---

As many of you probably know, Foursquare is a quasi-Geo-spatial social network, geared towards surfacing recommendations, location, and coordinated meetups. The end-user accomplishes this through a combination of texting, geo-tagging, and light content creation in the form of recommendations/reviews/etc. Often times the service is accessed via a mobile device, although one can engage in Foursquare activity through a desktop/laptop as well.

The end user activity is incentivized/rewarded through accumulation of badges, titles (A sort of Gamification), and through getting (what's hoped) activity appropriate/contextualized coupons/discounts/sometimes free goods that are machine determined (i.e. some matching procedure/algorithm produced). Also, there is an intrinsic element to the incentive, like Facebook, many foursquare power-users end up using the service because their immediate friends/social network also utilize the service (the so-called "Network effect").


---
