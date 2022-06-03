import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from '@angular/material/list';
import {MatButtonModule} from '@angular/material/button';
import { MatRadioModule} from '@angular/material/radio';
import { MatDatepickerModule} from '@angular/material/datepicker';
import { MatInputModule} from '@angular/material/input';
import { MatNativeDateModule} from '@angular/material/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';
import { AllteamComponent } from './pages/Teams/allteam/allteam.component';
import { AddteamComponent } from './pages/Teams/addteam/addteam.component';
import { AddtestimonialsComponent } from './pages/testimonials/addtestimonials/addtestimonials.component';
import { AlltestimonialsComponent } from './pages/testimonials/alltestimonials/alltestimonials.component';
import { AllpromocodeComponent } from './pages/promocode/allpromocode/allpromocode.component';
import { AddpromocodeComponent } from './pages/promocode/addpromocode/addpromocode.component';
import { AllcartitemsComponent } from './pages/allcartitem/allcartitems/allcartitems.component';
import { AllusersComponent } from './pages/newuser/allusers/allusers.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginService } from './services/login.service';
import { VehicleComponent } from './pages/vehicle/vehicle.component';
import { PaymentdetailsComponent } from './pages/payment/paymentdetails/paymentdetails.component';
import { AccountdetailsComponent } from './pages/payment/accountdetails/accountdetails.component';
import { CouponsComponent } from './pages/payment/coupons/coupons.component';
import { CustomuserComponent } from './pages/customuser/customuser/customuser.component';
import { SubscriptionComponent } from './pages/payment/subscription/subscription.component';
import { DropdetComponent } from './pages/dilevery/dropdet/dropdet.component';
import { InOrderComponent } from './pages/dilevery/in-order/in-order.component';
import { PickupdetComponent } from './pages/dilevery/pickupdet/pickupdet.component';
import { PlaceordComponent } from './pages/dilevery/placeord/placeord.component';
import { StateComponent } from './pages/dilevery/state/state.component';
import { StatusComponent } from './pages/dilevery/status/status.component';
import { UserroleComponent } from './pages/userrole/userrole/userrole.component';
import { DriverComponent } from './pages/Driver/driver/driver.component';

 
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MasterpageComponent,
    NewuserComponent,
    ImportuserComponent,
    AllproductComponent,
    AllteamComponent,
    AddteamComponent,
    AddtestimonialsComponent,
    AlltestimonialsComponent,
    AllpromocodeComponent,
    AddpromocodeComponent,
    AllcartitemsComponent,
    
    AllusersComponent,
          VehicleComponent,
          PaymentdetailsComponent,
          AccountdetailsComponent,
          CouponsComponent,
          CustomuserComponent,
          SubscriptionComponent,
          DropdetComponent,
          InOrderComponent,
          PickupdetComponent,
          PlaceordComponent,
          StateComponent,
          StatusComponent,
          UserroleComponent,
          DriverComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatButtonModule,
    MatRadioModule,
    MatDatepickerModule,
    MatInputModule,
    MatNativeDateModule,
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule,



  ],
  providers: [LoginService],
  bootstrap: [AppComponent]
})
export class AppModule { }
