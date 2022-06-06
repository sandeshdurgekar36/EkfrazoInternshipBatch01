import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustaddressComponent } from './pages/custaddres/custaddress/custaddress.component';
import { CustomuserComponent } from './pages/customuser/customuser/customuser.component';
import { DropdetComponent } from './pages/dilevery/dropdet/dropdet.component';
import { InOrderComponent } from './pages/dilevery/in-order/in-order.component';
import { PickupdetComponent } from './pages/dilevery/pickupdet/pickupdet.component';
import { PlaceordComponent } from './pages/dilevery/placeord/placeord.component';
import { StateComponent } from './pages/dilevery/state/state.component';
import { StatusComponent } from './pages/dilevery/status/status.component';
import { DriverComponent } from './pages/Driver/driver/driver.component';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { AllusersComponent } from './pages/newuser/allusers/allusers.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';
import { AccountdetailsComponent } from './pages/payment/accountdetails/accountdetails.component';
import { PaymentdetailsComponent } from './pages/payment/paymentdetails/paymentdetails.component';
import { SubscriptionComponent } from './pages/payment/subscription/subscription.component';
import { ReviewComponent } from './pages/review/review/review.component';
import { UserroleComponent } from './pages/userrole/userrole/userrole.component';
import { VehicleComponent } from './pages/vehicle/vehicle.component';


const routes: Routes = [
  {path:'',redirectTo:'login' , pathMatch:'full'},
  {path:'login',component:LoginComponent},
  {path:'masterpage',component:MasterpageComponent},
  {path:'newuser',component:NewuserComponent},
  {path:'importuser',component:ImportuserComponent},
  {path:'alluser',component:AllusersComponent},
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



];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
