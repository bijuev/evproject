"use strict";(self.webpackChunkevspot=self.webpackChunkevspot||[]).push([[209],{209:function(e,t,n){n.r(t),n.d(t,{default:function(){return v}});var o=n(439),i=n(791),a=n(716),l=[{featureType:"administrative",elementType:"labels.text.fill",stylers:[{color:"#535b69"}]},{featureType:"landscape",elementType:"all",stylers:[{color:"#f1f3ff"}]},{featureType:"poi",elementType:"all",stylers:[{visibility:"off"}]},{featureType:"road",elementType:"all",stylers:[{saturation:-100},{lightness:45}]},{featureType:"road.highway",elementType:"all",stylers:[{visibility:"simplified"}]},{featureType:"road.arterial",elementType:"labels.icon",stylers:[{visibility:"off"}]},{featureType:"transit",elementType:"all",stylers:[{visibility:"off"}]},{featureType:"water",elementType:"all",stylers:[{color:"#d5e0ff"},{visibility:"on"}]}],r=n(434),s=n(229),c=n(988),u=n(515),f=n(184),g=function(e){return(0,f.jsx)("button",{className:"current-btn",onClick:function(){navigator.geolocation.getCurrentPosition((function(t){e.onButtonClick(t.coords.latitude,t.coords.longitude)}))},children:(0,f.jsx)("svg",{xmlns:"http://www.w3.org/2000/svg",width:"30",height:"30",viewBox:"0 0 25 25",children:(0,f.jsx)("g",{id:"current",transform:"translate(-69.996 0)",children:(0,f.jsx)("path",{id:"Union_1","data-name":"Union 1",d:"M12.153,24.907a.694.694,0,0,1-.347-.6V20.8A8.333,8.333,0,0,1,4.2,13.194H.694a.694.694,0,0,1,0-1.389H4.2A8.333,8.333,0,0,1,11.806,4.2V.694a.694.694,0,0,1,1.389,0V4.2A8.333,8.333,0,0,1,20.8,11.806h3.5a.694.694,0,0,1,0,1.389H20.8A8.333,8.333,0,0,1,13.194,20.8v3.5a.694.694,0,0,1-1.042.6Zm.695-7.175a.694.694,0,0,1,.347.6v1.075a6.944,6.944,0,0,0,6.214-6.214H18.334a.694.694,0,1,1,0-1.389h1.075a6.944,6.944,0,0,0-6.214-6.214V6.667a.694.694,0,1,1-1.389,0V5.592a6.944,6.944,0,0,0-6.214,6.214H6.667a.694.694,0,1,1,0,1.389H5.592a6.944,6.944,0,0,0,6.214,6.214V18.333a.694.694,0,0,1,1.042-.6Zm-3-2.58a3.75,3.75,0,1,1,2.652,1.1A3.751,3.751,0,0,1,9.848,15.151Zm.982-4.321a2.361,2.361,0,0,0,1.67,4.031h0A2.361,2.361,0,1,0,10.83,10.83Z",transform:"translate(69.996 0)",fill:"currentColor"})})})})};var d=n.p+"static/media/plug.52a4018f7fa804ce68649e00e34ca8fb.svg",p=google.maps.TravelMode,v=function(){var e=(0,i.useState)(28.68469194538903),t=(0,o.Z)(e,2),n=t[0],v=t[1],m=(0,i.useState)(75.67244961643523),h=(0,o.Z)(m,2),y=h[0],w=h[1],x=(0,i.useState)(4),j=(0,o.Z)(x,2),L=j[0],b=j[1],T=(0,i.useState)(null),C=(0,o.Z)(T,2),Z=C[0],k=C[1],S=(0,i.useState)(null),E=(0,o.Z)(S,2),N=E[0],V=E[1],H=(0,i.useState)(!1),O=(0,o.Z)(H,2),A=O[0],G=O[1],I=(0,i.useState)(),K=(0,o.Z)(I,2),P=K[0],D=K[1],M=(0,r.I0)(),B=(0,r.v9)((function(e){return e.searchLocation.location})),z=(0,r.v9)((function(e){return e.direction.origin}),(function(e,t){return e.length===t.length})),F=(0,r.v9)((function(e){return e.direction.destination}),(function(e,t){return e.length===t.length})),R=(0,r.v9)((function(e){return e.markers.positions})),U=(0,r.v9)((function(e){return e.nearbyCenter.center})),_=(0,u.Z)().launchNavigation,q=(0,c.Z)(),J=q.lat,Q=q.lng,W=q.error,X=q.status,Y=q.getGeocode,$=(0,c.Z)(),ee=$.lat,te=$.lng,ne=($.error,$.status),oe=$.getGeocode,ie=(0,c.Z)(),ae=ie.lat,le=ie.lng,re=(ie.error,ie.status),se=ie.getGeocode;(0,i.useEffect)((function(){"OK"===X?(v(J),w(Q),b(10),G(!0)):console.log(W)}),[J,Q,X]),(0,i.useEffect)((function(){Y(B)}),[B]),(0,i.useEffect)((function(){oe(z)}),[z]),(0,i.useEffect)((function(){se(F)}),[F]),(0,i.useEffect)((function(){if("OK"===ne&&"OK"===re){var e=new google.maps.DirectionsService,t=new google.maps.LatLng(ee,te),n=new google.maps.LatLng(ae,le);e.route({origin:t,destination:n,travelMode:p.DRIVING},(function(e,t){if("OK"===t){k(e);var n=new window.google.maps.Polyline({path:null===e||void 0===e?void 0:e.routes[0].overview_path}),o=R.filter((function(e,t){return window.google.maps.geometry.poly.isLocationOnEdge(new window.google.maps.LatLng(e.lat,e.lng),n,.01)}));V(o)}}))}}),[ee,te,ne,ae,le,re]),(0,i.useEffect)((function(){if(N&&N.length>0){M(s.f.stopOverPoints({stopPoints:N}));var e=new google.maps.DirectionsService,t=new google.maps.LatLng(ee,te),n=new google.maps.LatLng(ae,le),o=N.map((function(e,t){return{location:new google.maps.LatLng(e.lat,e.lng),stopover:!1}}));e.route({origin:t,destination:n,travelMode:p.DRIVING,waypoints:o},(function(e,t){"OK"===t&&k(e)}))}}),[N]);var ce={styles:l};(0,i.useEffect)((function(){U.lat&&U.lng&&(v(U.lat),w(U.lng),b(13),G(!0))}),[U]);return(0,f.jsx)(i.Fragment,{children:(0,f.jsxs)("div",{className:"position-relative",children:[(0,f.jsx)(g,{onButtonClick:function(e,t){v(e),w(t),b(10),G(!0)}}),(0,f.jsxs)(a.b6,{mapContainerStyle:{width:"100%",height:"calc(100vh - 64px)"},center:{lat:n,lng:y},zoom:L,options:ce,children:[R.map((function(e,t){return(0,f.jsx)(a.jC,{position:e,icon:{url:d},onClick:function(){return D(e)}},t)})),A&&(0,f.jsx)(a.jC,{position:{lat:n,lng:y}}),Z&&(0,f.jsx)(a.tH,{directions:Z}),!!P&&(0,f.jsx)(i.Fragment,{children:(0,f.jsx)(a.nx,{position:{lat:null===P||void 0===P?void 0:P.lat,lng:null===P||void 0===P?void 0:P.lng},zIndex:99,onCloseClick:function(){return D(null)},children:(0,f.jsxs)("div",{className:"map-popup mxw-6",children:[(0,f.jsx)("div",{className:"title",children:P.title}),(0,f.jsx)("div",{className:"address",children:P.address}),(0,f.jsx)("button",{onClick:function(e,t){navigator.geolocation.getCurrentPosition((function(n){var o=new google.maps.LatLng(n.coords.latitude,n.coords.longitude),i=new google.maps.LatLng(e,t);_(o,i)}))}.bind(undefined,P.lat,P.lng),children:"Get direction"})]})})})]})]})})}}}]);
//# sourceMappingURL=209.09da2e2e.chunk.js.map