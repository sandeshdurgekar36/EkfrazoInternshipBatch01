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
  providers: [LoginService,UserroleService,SubsriptionService,VehiclesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
