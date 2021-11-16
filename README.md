## Table of Contents:

- [UX](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Features](#features)
  - [Deployed Features](#deployed-features)
  - [Features to consider implementing in the future](#features-to-consider-implementing-in-the-future)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks and Tools](#frameworks-and-tools)
  - [Workspace and Related Tools](#workspace-and-related-tools)
- [Resources](#resources)
- [Code Validation Tools](#code-validation-tools)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgments](#acknowledgments)

## UX

### User Stories
<hr>

### Viewing and Navigation:
|  | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
1| Shopper| View a list of products available | Browse and select items to purchase |
2| Shopper | View individual product details | View specific product information |
3| Shopper | Easily see featured items and promotions | Make sure not to miss out on promotions |
4| Shopper | Save products for purchase later | Add products to a wishlist for future purchasing |

### Registration and User Accounts
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
5| Site User | Easily register for an account | Have personal account that saves my information |
6| Site User | Easily Login or Logout | Access my profile with standard login |
7| Site User | Verify my account has been successfully created | Receive an email confirming account linked |
8| Site User | Have a personalized user profile | View my order history, personal information and wishlist |

### Registered User Extra Functionality
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
9| Registered User | Add product reviews | Voice my recomendations on a product |
10| Registered User | Edit/Update my review | Edit review if mistakes shown or new information to add |
11| Registered User | Delete my review | Delete my review if i do not want is shared any longer |
12| Registered User | Add products to my wishlist | Somewhere i can save products i am interested in purchasing at a later date |
13| Registered User | Transfer items from my wishlist to my shopping bag | Easy add to bag button from wishlist |
14| Registered User | Remove items from my wishlist | Delete item if i no longer want or have aquired elsewhere |

### Sorting and Searching
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
15| Shopper | Sort/filter the list of available products | Find the products I want, by name, price or category |
16| Shopper | Have seperation on product types | Only see certain product types on particular pages |
17| Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |

### Subscribers
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
18| Subscriber | Join subscription service to receive new music every month | Add to music as a surprise to my collection |
19| Subscribers | Narrow down possible vinyl sent by selection genre | Ensures the subscription vinyl sent is close to my interests |

### Purchasing and Checkout
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
20| Shopper | Ability to update quantities in the shopping bag | Allow to add additional quantites of items or remove some |
21| Shopper | Clearly see an order summary before checkout | Finl check on items and prices |
22| Shopper | Easily enter my shipping and payment information | Seemless checkout experience |
23| Shopper | See order confirmation post purchase | Verify that the purchase was a success |
24| Shopper | Receive email confirmation | Double verification that the order was a success |

### Store Owner or Product Manager
| User No. | As a... | I want to be able to... | So that I can... |
|----|:--------|:------------------------|:-----------------|
25| Store Owner | Add a product | Add new products to my store |
26| Store Owner | Edit and update a product | Easily change all product information |
27| Store Owner | Delete a product | Remove items if no longer an option |

### Strategy
- Provide a platform where users can find new music in vinyl form
- Provide a platform where users can purchase new vinyls
- Provide a platform where users can purchase HI-FI systems for playing vinyls
- Provide a blog space for curated record reviews for products purchasable on the same store

### Scope 
- An easy to navigate site with simple register, login and logout functions
- A smooth checkout experience utilisinh Stripe
- A wishlist so users can come back to products they are interested in

### Structure
I wanted to create a simple and distraction free platform where the user experience and attention is always kept and directed towards the products being sold. 
For this reason the functionality is limited to only essential functions.
The structure and layout of pages is very similar across the board and allows for easy navigation without distraction

### Skeleton
- [Wireframes](readme-docs/wireframes/wireframes.pdf) - The final commit has not differed much from the initial intentions highlighted in the wireframes
- Navigation Bar
- - Home - Homepage containing call to action, blurb on purpose of site and a few featured articles
- - Articles - Call to action to post article with articles below catagorised by topic on different tabs
- - Post Article - Form to contribute an article including TinyMCE textarea
- - Article - Article page displaying topic, image, author, date published and the article body with a comments section at the bottom
- - Login - Simple login form requesting username and password. Link at bottom of form to register if not already
- - Register - Simple register form requesting full name, email address, username and password. Link at bottom of form to login if already registered
- - Profile - Contains all articles contributed by user with buttons to read, edit and delete articles. Delete articles propmts a modal to make sure the user wants to delete
- - Edit - Allows user to edit article with pre-populated fields containing original article
-
#### Database Diagram
![Project Across Devices](static/docs/database-diagram.png)

### Surface
The intention for the design was to keep everything simple and not take away from the content
#### Colours
The base colour was kept as white #fafafa with #545454 used for most fonts. There is some colour added on buttons but generally the main colour on the site comes from the images throughout which are supposed to represent blockchain related tech and imagery
#### Fonts
I used the proxima-nova font with 300 weighting and sans-serif as backup


## User Stories

