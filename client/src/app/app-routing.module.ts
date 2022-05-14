import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddnewprComponent } from './pages/addnewpr/addnewpr/addnewpr.component';
import { AllcartitemsComponent } from './pages/allcartitem/allcartitems/allcartitems.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { AllusersComponent } from './pages/newuser/allusers/allusers.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';
import { AddpromocodeComponent } from './pages/promocode/addpromocode/addpromocode.component';
import { AllpromocodeComponent } from './pages/promocode/allpromocode/allpromocode.component';
import { AddteamComponent } from './pages/Teams/addteam/addteam.component';
import { AllteamComponent } from './pages/Teams/allteam/allteam.component';
import { AddtestimonialsComponent } from './pages/testimonials/addtestimonials/addtestimonials.component';
import { AlltestimonialsComponent } from './pages/testimonials/alltestimonials/alltestimonials.component';

const routes: Routes = [
  {path:'login',component:LoginComponent},
  {path:'masterpage',component:MasterpageComponent},
  {path:'newuser',component:NewuserComponent},
  {path:'importuser',component:ImportuserComponent},
  {path:'alluser',component:AllusersComponent},
  {path:'addnewpr',component:AddnewprComponent},
  {path:'allproduct',component:AllproductComponent},
  {path:'allteam',component:AllteamComponent},
  {path:'addteam',component:AddteamComponent},
  {path:'alltestimonials',component:AlltestimonialsComponent},
  {path:'addtestimonials',component:AddtestimonialsComponent},
  {path:'allcartitem',component:AllcartitemsComponent},
  {path:'addpromocode',component:AddpromocodeComponent},
  {path:'allpromocode',component:AllpromocodeComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
