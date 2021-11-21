## User Stories Testing
### Viewing and Navigation
1. View a list of products available to be able to browse and select items to purchase
- Press Records has multiple categories of products which can be viewed together under all products or filtered by category or artist for vinyls.
2. View individual product details to view specific product information
- Each product contains an image, description and pricing information to inform purchases
3. Easily see featured items and promotions to not miss out on deals
- Our home page contains two carousels, one for featured products and another for HI-FI deals
4. Save products by adding products to a wishlist for future purchasing
- When a user has created an account, they can save products to their wishlist and add straight to their bag from the wishlist at a later date
### Registration and User Accounts
5. Easily register for an account so i can save my information
- I have utilised Django Allauth to streamline and simplify the registration process
6. Easily login and logout so i can easily access my account
- Again, Allauth has simplified the login and logout process
7. Verify my account has been created by receiving a confirmation email
- When registered, an email will be sent to the supplied email address requiring the user to follow a link to verify the email address
8. Have a personalised user account so i can view order history, personal information and my wishlist
- When a user registers, they can save their shipping information in their account, access past orders when one has been made and save products to a wishlist for shopping later
### Registered User Extra Functionality
9. Add products to my wishlist so i can purchase at a later date
- Registered users can add a product to their wishlist from the products page.
10. Transfer items from wishlist to my bag so i can easily purchase the product
- On the wishlist page, each product has the ability to be added directly into the shopping bag
11. Remove item from wishlist if i no long want to purchase ot have aquired elsewhere
- On the wishlist page, each item has a button to remove from the wishlist
### Sorting ans Searching
12. Soft/filter the list of available products by name or price
- The products page has a sort bar where you can sort by name alphabetically or by price
13. Have seperation on product types so i can only see the things i am interested in.
- From the main side navigation you can choose from the three categories or products we sell and be brought to the products page only displaying these
14. Search for a product by name or artist so i can find the specific product i am looking for
- In the side navigation bar there is a search bar which will search across our rage of products for the term entered
### Purchasing and Checkout
15. Ability to update products in the shoping bag so i can add an extra of a product or remove one if i have too many
- The shopping bag has a quantity selector beside each product along with a button to remove from bag
16. Clearly see an order summary before checkout so i can have a final check on prices and items
- At the checkout page, there is a simple order summary so you can double check everything before purchase
17. Easily enter my shipping and payment information for a seemless checkout experience
- The site utilised crispy forms and Stripe to ensure a clean and smooth checkout process
18. See order conformation post purchase so i can verify it was a success
- Once the payment has been made, users are directed to a order summary page which summarises costs, shipping details etc
19. Receive email confirmation so that i can double check my order was a success
- The user will receive order confirmation on their order shortly after pruchasing
### Store Owner or Product Manager
20. Add a new product to my store
- The owner can add new products directly from the Product Management page under My Account on the nav bar
21. Edit and update products so i can easily change all product information
- All product information can be updated by clicking the edit button on a product page and ammending the product form
22. Delete a product so i can remove a product we no longer sell
- from the products page, the owner can delete a product from the site
23. Add a blog post about items we sell.
- The owner can add a blog post from the Blog Management page under My Account on the nav bar but for now it is advised to do this through the Django admin. This is due to the fact that as of now there is no WYSIWYG editor built into the site but one is enabled in the Django admin. There is a link to the admin on the Blog Management page
24. Edit and update a blog post so i can easily change information.
- Again, it is recommended to visit the Django admin's blog section, choose the blog to update and edit from there with the WYSIWYG editor
25. Delete a blog if it is no longer relevant
- The owner can delete a blog post from the blog post's page

## Automated View Testing
- I wrote automated testing for the majority of the views across the site. View testing ws written to ensure the correct template was being passed along with the correct HttpResponse codes. Tests were also written for adding, updating and deleting the shopping bag and also the CRUD functionality for the blog app.

- Python Coverage has been installed and can be run in a cloned repository to view coverage reports

## Manual Navigation Link Testing
**Nav Bar**
- Checked all nav bar items direct user to correct page including logo returning to home
- Checked that My Account and Wishlist only displays to logged in users
- Checked Shop by category filters content correctly
- Checked that the shopping bag link takes users to the shopping bag

**Home Page**
- Checked call to action routes to the products page
- Checked clicking the product displayed in the caurosel takes you to the correct product page
- Checked that the category section routes to the correct filtered products page
- Checked social links open in a new tab

**Register**
- Checked Already Registered link directs to the login page

**Login**
- Checked Not Registered link directs to the registration page

**Products**
- Checked that by clicking a product users are directed to the specific product detail page
- Checked that by clicking an artist name users are directed to the artists page

**Shopping Bag**
- Checked that Checkout takes users to the checkout page
- Checked that 'Keep Shopping' returns users to the products page

**Account**
- Checked that by clicking on the order number in past orders, users are taken to a summary of that order

**Blog**
- Checked that by clicking on a blog image users are taken to that particular post

## Page Functionality Testing - User
### Nav Bar
- Checked that Login and Register appear if no user is logged in
- Checked that Account, Wishlist and Logout appear if user is signed in

### Register
- Checked message appears if user tries to register with an existing username
- Checked email field requires email formatting

### Login
- Checked messages states username/password incorrect if user fails to login

### Logout
- Checked that logout button returns to home page

### Profile
- Checked that user can save updated shipping information from the profile

### Wishlist
- Checked that users can add item to bag from wishlist
- Checked that users can remove items from wishlist

### Product
- Checked that users can add products with choosen quantity to bag

### Shopping Bag
- Checked that users can update item quantity
- Checked that users can remove item from bag
- Checked that users can proceed to checkout with items in bag

### Checkout
- Checked that users can fill in shipping details
- Checked that shipping details carry from Account if already saved their
- Checked that users can successfully process a purchase
    - All purchases were tested using the Stripe test card
    - 4242 4242 4242 4242 02/24 242 12345

## Page Functionality Testing - Owner
### Products
- Checked owner can successfully add a product
- Checked that owner can edit a product and save the updated information
- Check that owners can delete a product from the store

### Blogs
- Checked owner can successfully add a blog post. As mentioned in readme.md, blogs should be added from the Django Admin for now
- Checked that owner can edit a blog and save the updated information
- Check that owners can delete a blog from the store

### 404 Page
- Checked route is working as intended and 404 page is displayed if invalid link entered
- Checked Return to Home button reirects to the home page

## Responsiveness
Responsiveness was checked using [Responsinator](https://www.responsinator.com/) while also designed with responsiveness in mind with regular testing on Dev Tools. The responsiveness has been tested across multiple devices such as iPhone 8, iPhone 8 Plus, iPhone X, Samusing Galaxy X5, iPad etc. on the Responsinator site.


## Performance
I tested the performance of the app with Lighthouse. At this point, the 'Performance' results on the were not satisfactory. This is mainly due to serving images too large for the carousels. The majority of the other pages are scoring highly however. I am to fix the image serving issue at a later date but ran out of time before submission