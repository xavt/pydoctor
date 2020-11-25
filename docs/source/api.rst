
API Reference
=============

.. Configuration from https://setupdocx.sourceforge.io/configurations/epydoc/epydoc_sphinx_iframe/index.html

.. raw:: html

   <style>
      div[aria-label^=breadcrumbs], footer, #api-reference h1 {
         display: none;
      }
      div.wy-nav-content {
          padding: 0px 0px 0px 0px;
          max-width: 100%;
      }
      div.iapiref {
          position: relative;
      }
      iframe.iapiref  {
          position: absolute;
          top: 0;
          width: 100%;
      }
   </style>

   <script>
      document.body.onload = function(o){
          document.getElementById("glu").style.height = document.body.scrollHeight+"px";
      }
      document.body.onresize = function(o){
         document.getElementById("glu").style.height = document.body.scrollHeight+"px";
      }
   </script>  
   
   <div class="iapiref">
      <iframe id='glu'
         class="iapiref"
         src="api/index.html"
         allowfullscreen
      ></iframe>
   </div>