import '../ComponentsCss/MenuIcon.css'
import React from 'react';
const MenuIcon=()=>{
 const [open,setOpen]= React.useState(false);
console.log(open);
 return(
    <div class={"whole-icon"+(open?" change":null)} onClick={()=>{setOpen(!open)}}>
  <div class="bar1"></div>
  <div class="bar2"></div>
  <div class="bar3"></div>
</div>
 )
}
export default MenuIcon;