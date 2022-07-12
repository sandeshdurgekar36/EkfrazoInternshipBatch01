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
import { ReviewComponent } from './pages/review/review/review.component';
import { CustaddressComponent } from './pages/custaddres/custaddress/custaddress.component';
import { UserroleService } from './services/userrole.service';
import { SubsriptionService } from './services/subsription.service';
import { VehiclesService } from './services/vehicles.service';
import { StateService } from './services/state.service';
import { StatusService } from './services/status.service';
import { PlaceordService } from './services/placeord.service';
import { PickupdetService } from './services/pickupdet.service';
import { InordService } from './services/inord.service';
import { DropdetService } from './services/dropdet.service';
import { AccountService } from './services/account.service';
import { PaymentdetService } from './services/paymentdet.service';
import { ReviewService } from './services/review.service';
import { DriverService } from './services/driver.service';
import { CustomusertComponent } from './pages/tables/customusert/customusert.component';
import { DrivertComponent } from './pages/tables/drivert/drivert.component';
import { CustomaddtComponent } from './pages/tables/customaddt/customaddt.component';
import { DileverytComponent } from './pages/tables/dileveryt/dileveryt.component';
import { CouponstComponent } from './pages/tables/couponst/couponst.component';
import { StaustComponent } from './pages/tables/staust/staust.component';
import { StatetComponent } from './pages/tables/statet/statet.component';

 
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MasterpageComponent,
    NewuserComponent,
    ImportuserComponent,    
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
          ReviewComponent,
          CustaddressComponent,
          CustomusertComponent,
          DrivertComponent,
          CustomaddtComponent,
          DileverytComponent,
          CouponstComponent,
          StaustComponent,
          StatetComponent,
          CustomusertComponent
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
  providers: [LoginService,UserroleService,SubsriptionService,VehiclesService,StateService,StatusService,PlaceordService,PickupdetService,InordService,DropdetService,AccountService,PaymentdetService,ReviewService,DriverService],
  bootstrap: [AppComponent]
})
export class AppModule { }
