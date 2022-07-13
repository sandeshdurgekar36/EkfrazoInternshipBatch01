import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddnewprComponent } from './pages/addnewpr/addnewpr/addnewpr.component';
import { AllcartitemsComponent } from './pages/allcartitem/allcartitems/allcartitems.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { AllusersComponent } from './pages/newuser/allusers/allusers.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';
<<<<<<< HEAD
import { AddpromocodeComponent } from './pages/promocode/addpromocode/addpromocode.component';
import { AllpromocodeComponent } from './pages/promocode/allpromocode/allpromocode.component';
import { AddteamComponent } from './pages/Teams/addteam/addteam.component';
import { AllteamComponent } from './pages/Teams/allteam/allteam.component';
import { AddtestimonialsComponent } from './pages/testimonials/addtestimonials/addtestimonials.component';
import { AlltestimonialsComponent } from './pages/testimonials/alltestimonials/alltestimonials.component';
=======
import { AccountdetailsComponent } from './pages/payment/accountdetails/accountdetails.component';
import { CouponsComponent } from './pages/payment/coupons/coupons.component';
import { PaymentdetailsComponent } from './pages/payment/paymentdetails/paymentdetails.component';
import { SubscriptionComponent } from './pages/payment/subscription/subscription.component';
import { ReviewComponent } from './pages/review/review/review.component';
import { UserroleComponent } from './pages/userrole/userrole/userrole.component';
import { VehicleComponent } from './pages/vehicle/vehicle.component';
import { CustomusertComponent } from './pages/tables/customusert/customusert.component'; 

>>>>>>> 6fc0f60b6683a1c5a200dc2360fb80bb5c99a16c

const routes: Routes = [
  {path:'',component:HomeComponent},
  {path:'login',component:LoginComponent},
  {path:'masterpage',component:MasterpageComponent},
  {path:'newuser',component:NewuserComponent},
  {path:'importuser',component:ImportuserComponent},
  {path:'alluser',component:AllusersComponent},
<<<<<<< HEAD
  {path:'addnewpr',component:AddnewprComponent},
  {path:'allproduct',component:AllproductComponent},
  {path:'allteam',component:AllteamComponent},
  {path:'addteam',component:AddteamComponent},
  {path:'alltestimonials',component:AlltestimonialsComponent},
  {path:'addtestimonials',component:AddtestimonialsComponent},
  {path:'allcartitem',component:AllcartitemsComponent},
  {path:'addpromocode',component:AddpromocodeComponent},
  {path:'allpromocode',component:AllpromocodeComponent},
=======
  {path:'vehicle',component:VehicleComponent},
  {path:'customuser',component:CustomuserComponent},
  {path:'state',component:StateComponent},
  {path:'status',component:StatusComponent},
  {path:'subscription',component:SubscriptionComponent},
  {path:'userrole',component:UserroleComponent},
  {path:'placeord',component:PlaceordComponent},
  {path:'in-order',component:InOrderComponent},
  {path:'paymentdetails',component:PaymentdetailsComponent},
  {path:'driver',component:DriverComponent},
  {path:'accountdetails',component:AccountdetailsComponent},
  {path:'custaddress',component:CustaddressComponent},
  {path:'dropdet',component:DropdetComponent},
  {path:'pickupdet',component:PickupdetComponent},
  {path:'review',component:ReviewComponent},
  {path:'coupons',component:CouponsComponent},
  {path:'customusert',component:CustomusertComponent},


>>>>>>> 6fc0f60b6683a1c5a200dc2360fb80bb5c99a16c

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
