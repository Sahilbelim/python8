from bs4 import BeautifulSoup

html=''' <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <h1 class="display-3 text-center">Exercise</h1>

    <div class="container-fluid">
      <div class="row">
        <div class="col-12 col-md-3 col-lg-4 col-sm-6 mt-5">
          <p class="lead" id ='p-3'>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla
            temporibus dolorem nostrum! Nulla a atque recusandae quod commodi
            provident Lorem ipsum dolor sit amet.
          </p>
        </div>
        <div class="col-12 col-lg-3 col-md-4 col-sm-6 mt-5">

          <h1>this is heading <span> <b>ok</b></span></h1>
          <p class="lead">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias
            iure repellat non obcaecati tempore adipisci facere corrupti
            accusantium molestiae reprehenderit inventore, laboriosam cum
            provident eveniet maiores neque, natus magni illum.
          </p>
        </div>
        <div class="col-12 col-lg-3 col-md-4 col-sm-6 mt-5">
          <p class="lead">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias
            iure repellat non obcaecati tempore adipisci facere corrupti
            accusantium molestiae reprehenderit inventore, laboriosam cum
            provident eveniet maiores neque, natus magni illum.
          </p>
        </div>

        <div class="col-12 col-md-3 col-lg-4 col-sm-6 mt-5">
          <p class="lead">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias
            iure repellat non obcaecati tempore adipisci facere corrupti
            accusantium molestiae reprehenderit inventore, laboriosam cum
            provident eveniet maiores neque, natus magni illum.
          </p>
        </div>
      </div>
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
'''

doc_html=BeautifulSoup(html,'html.parser')
# print(doc_html)

# formated_html=doc_html.prettify()
# print(formated_html)

# print(doc_html.span)
h1List=doc_html.b
# singleh1=h1List[1]
print(h1List.string)