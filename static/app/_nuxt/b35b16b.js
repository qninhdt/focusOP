(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{290:function(e,t,n){var content=n(294);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(7).default)("64617f91",content,!0,{sourceMap:!1})},293:function(e,t,n){"use strict";n(290)},294:function(e,t,n){var c=n(6)(!1);c.push([e.i,"#device{text-align:center;width:45%;margin:10% auto auto}#device a{padding:1rem 30%}.device-icon{height:2rem;margin:0 1rem}",""]),e.exports=c},323:function(e,t,n){"use strict";n.r(t);var c={"Iriun Webcam":"iriuncam.png","DroidCam Source 2":"droidcam.png","DroidCam Source 3":"droidcam.png","EpocCam Camera":"epoccam.png",Default:"camera.png"},o={data:function(){return{devices:[]}},mounted:function(){var e=this;this.$socket.emit("get_devices",(function(t){e.devices=t}))},methods:{icon:function(e){return e in c?c[e]:c.Default},connect:function(e){this.$socket.emit("set_device",e),document.location.href="/app/explore"}}},r=(n(293),n(2)),component=Object(r.a)(o,(function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("nav",{staticClass:"panel",attrs:{id:"device"}},[n("p",{staticClass:"panel-heading",staticStyle:{color:"#be2edd"}},[e._v("\n            Lựa chọn thiết bị\n        ")]),e._v(" "),e._l(e.devices,(function(t,i){return n("a",{key:i,staticClass:"panel-block",on:{click:function(t){return e.connect(i)}}},[n("span",{staticClass:"panel-icon"}),e._v(" "),n("img",{staticClass:"device-icon",attrs:{src:"/app/public/"+e.icon(t),alt:t}}),e._v("\n            "+e._s(t)+"\n        ")])}))],2)])}),[],!1,null,null,null);t.default=component.exports}}]);