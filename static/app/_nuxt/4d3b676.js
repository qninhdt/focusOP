(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{283:function(t,e,r){var content=r(285);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,r(8).default)("4b3378e2",content,!0,{sourceMap:!1})},284:function(t,e,r){"use strict";r(283)},285:function(t,e,r){var o=r(7)(!1);o.push([t.i,'.fop-file{display:inline-block;position:relative;margin:1rem;width:calc(15rem + 50px);height:calc(10rem + 30px);box-shadow:.5rem .6rem hsla(0,0%,50.2%,.2);border-bottom:3px solid #e056fd}.fop-file:before{content:"";position:absolute;left:0;right:0;top:0;bottom:0;background:rgba(236,240,241,.49412)}.fop-file .info{height:30%;position:absolute;bottom:0;width:100%;background:#f5f5f5;padding:.5rem}.fop-file:hover .info{background-color:#e056fd;color:#fff;transition-duration:.3s}.fop-file:hover{transform:translateY(.2rem);transition-duration:.5s;box-shadow:.4rem .5rem hsla(0,0%,50.2%,.2)}',""]),t.exports=o},286:function(t,e,r){"use strict";var o={props:["filename"]},n=(r(284),r(2)),component=Object(n.a)(o,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("nuxt-link",{attrs:{to:"/explore/"+t.filename}},[r("div",{staticClass:"fop-file",staticStyle:{background:"url(http://www.builderwebsitedesigns.com/wp-content/uploads/2017/06/1-1.jpg)","background-size":"cover"}},[r("div",{staticClass:"info"},[r("h3",[t._v(t._s(t.filename))])])])])}),[],!1,null,null,null);e.a=component.exports},288:function(t,e,r){var content=r(316);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,r(8).default)("85387a1a",content,!0,{sourceMap:!1})},315:function(t,e,r){"use strict";r(288)},316:function(t,e,r){var o=r(7)(!1);o.push([t.i,"@import url(https://fonts.googleapis.com/css2?family=KoHo:wght@400&display=swap);"]),o.push([t.i,'.reveal{color:#22a6b3;height:100vh!important;cursor:none;font-size:2rem!important;font-family:"KoHo",sans-serif}.reveal,.reveal-viewport{background:transparent!important}.reveal .slide-background{background-color:transparent!important}#cursor{z-index:999;position:absolute;height:10px;width:10px;border:3px solid;border-radius:100%}#background{position:absolute;top:0;left:0;display:block;z-index:-2}.MathJax_Display{margin:.5rem 0!important}.reveal p{text-align:left;position:relative}.reveal ol,.reveal ul{display:block}.reveal pre{padding:0!important}.reveal p:before{content:"";position:absolute;width:1rem;height:.1rem;background:#000;top:1.5rem;left:-1.5rem}#logo{position:absolute;top:1rem;left:1rem}@-webkit-keyframes rotating{0%{transform:rotate(-1turn)}to{transform:rotate(0deg)}}@keyframes rotating{0%{transform:rotate(-1turn)}to{transform:rotate(0deg)}}.rotating{-webkit-animation:rotating 5s linear infinite;animation:rotating 5s linear infinite}.reveal .hljs::-webkit-scrollbar{background:transparent;width:.3rem}.reveal .hljs::-webkit-scrollbar-thumb{background:hsla(0,0%,67.5%,.2);border-radius:.15rem}.reveal .hljs::-webkit-scrollbar-thumb:hover{background:hsla(0,0%,50.6%,.2)}.square{width:2vw;height:2vw;background-color:#000;position:absolute;z-index:9999}#square-1{top:1vw;right:1vw}#square-2{left:1vw;bottom:1vw}',""]),t.exports=o},318:function(t,e,r){"use strict";r.r(e);var o,n=r(4),l=(r(37),r(291)),c=r(292),f=(r(293),r(295),r(309)),d=r.n(f),m=r(310),h=r.n(m),v=(r(311),r(312),r(313),r(129)),w=r.n(v),x={components:{File:r(286).a},head:function(data){return{title:"FocusOP ― "+data.filename}},data:function(){return{text:"",hand_type:"",cursor:[0,0]}},asyncData:function(t){return Object(n.a)(regeneratorRuntime.mark((function e(){var r,o;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.params,o=r.filename,e.abrupt("return",{filename:o});case 3:case"end":return e.stop()}}),e)})))()},mounted:function(){var t=this;return Object(n.a)(regeneratorRuntime.mark((function e(){var cursor;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:o=new l.a({plugins:[c.a,d.a,h.a],math:{mathjax:"https://cdn.jsdelivr.net/gh/mathjax/mathjax@2.7.8/MathJax.js",config:"TeX-AMS_HTML-full"}}),t.$socket.emit("get_fop",t.filename,function(){var e=Object(n.a)(regeneratorRuntime.mark((function e(text){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t.text=text,e.next=3,t.$nextTick();case 3:return e.next=5,o.initialize();case 5:w.a.init({selector:"#background",connectParticles:!0,color:["#e056fd","#ff9ff3"],minDistance:75,maxParticles:75});case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()),window.hand={},t.$socket.on("new_hand_dir",(function(t){"left"==t&&o.left(),"right"==t&&o.right()})),cursor=document.getElementById("cursor"),document.addEventListener("mousemove",(function(t){cursor.style.left=t.clientX+"px",cursor.style.top=t.clientY+"px"})),t.$socket.on("new_hand_type",(function(e){window.hand=e,t.hand_type=e.label}));case 7:case"end":return e.stop()}}),e)})))()},computed:{cursorColor:function(){return"CONTROL"==this.hand_type?["#f39c12","#f39c12"]:["#e74c3c","#e74c3c"]}}},k=(r(315),r(2)),component=Object(k.a)(x,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticStyle:{height:"100vh",width:"100vw"}},[r("span",{style:{borderColor:t.cursorColor[0],backgroundColor:t.cursorColor[1]},attrs:{id:"cursor"}}),t._v(" "),r("img",{staticClass:"rotating",attrs:{id:"logo",width:"40px",height:"40px",src:"/app/public/logo.png"}}),t._v(" "),r("div",{staticClass:"reveal",domProps:{innerHTML:t._s(t.text)}}),t._v(" "),r("canvas",{attrs:{id:"background"}}),t._v(" "),r("div",{staticClass:"square",attrs:{id:"square-1"}}),t._v(" "),r("div",{staticClass:"square",attrs:{id:"square-2"}})])}),[],!1,null,null,null);e.default=component.exports}}]);