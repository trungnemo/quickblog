# Layout the Index

- Draft the MAIN layout of the index.html

## Layout the index.html

- Index page will have 2 main parts: The Left and the Right pane
- The left will host the form to add a post. It will take 1/3 of the WHOLE PAGE
- The Right will list all the posts , it will take 2/3 of the WHOLE PAGE, and on the right

```html
{% block content %}
    <div class="container">
        <!--The row contains 12 cols of bootstrap-->
        <div class="row mt-5 pt-5">
            <!--The Left Pain: for the Menu: it takes 4 columns-->
            <div class="col-md-4">

            </div>
            <!--The Right Pain: for Post Index: it takes 8 columns-->
            <div class="col-md-8">

            </div>
        </div>
    </div>
    {% endblock %}
```
We layout the Post listing page (the Right pane)

- We use the card, and card body bootstrap body
- In the card body, we add row for each post
- In each row, we add col-md-4 for the post image, and col-md-8 for the post title and text
```html
 
<!--Index Content -->
{% block content %}
<div class="container">
        <!--The row contains 12 cols of bootstrap-->
        <div class="row mt-0 pt-5">
            <!--The Left Pain: for the Menu: it takes 4 columns-->
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body shadow">
                        <h3>Add a Post Form here</h3>
                    </div>
                </div>
            </div>
            <!--The Right Pain: for Post Index: it takes 8 columns-->
            <div class="col-md-8">
                <!--We use the card for each post-->
                <div class="card">
                    <div class="card-body">
                        <!--A Post 1 -->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>28th Sept 2021</small>
                                    <hr/>
                                    <a class="h3" href="">Ben Post 1</a>
                                    <p class="text-justify p-3">
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta illum commodi accusamus est dicta explicabo maiores architecto temporibus aperiam incidunt iure vero, fugiat quo beatae sit ullam voluptatum laboriosam ex!
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                         <!--A Post 2-->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>28th Sept 2021</small>
                                    <hr/>
                                    <a class="h3" href="">Ben Post 2</a>
                                    <p class="text-justify p-3">
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta illum commodi accusamus est dicta explicabo maiores architecto temporibus aperiam incidunt iure vero, fugiat quo beatae sit ullam voluptatum laboriosam ex!
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                          <!--A Post 3-->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>28th Sept 2021</small>
                                    <hr/>
                                    <a class="h3" href="">Ben Post 3</a>
                                    <p class="text-justify p-3">
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta illum commodi accusamus est dicta explicabo maiores architecto temporibus aperiam incidunt iure vero, fugiat quo beatae sit ullam voluptatum laboriosam ex!
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```
- Run the web server to test the layput of index.html
```bash
python manage.py runserver
```
## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
