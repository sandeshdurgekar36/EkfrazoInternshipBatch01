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
import { AddnewprComponent } from './pages/addnewpr/addnewpr/addnewpr.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';
import { AllteamComponent } from './pages/Teams/allteam/allteam.component';
import { AddteamComponent } from './pages/Teams/addteam/addteam.component';
import { AddtestimonialsComponent } from './pages/testimonials/addtestimonials/addtestimonials.component';
import { AlltestimonialsComponent } from './pages/testimonials/alltestimonials/alltestimonials.component';
import { AllpromocodeComponent } from './pages/promocode/allpromocode/allpromocode.component';
import { AddpromocodeComponent } from './pages/promocode/addpromocode/addpromocode.component';
import { AllcartitemsComponent } from './pages/allcartitem/allcartitems/allcartitems.component';
import { AllusersComponent } from './pages/newuser/allusers/allusers.component';

 
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MasterpageComponent,
    NewuserComponent,
    ImportuserComponent,
    AddnewprComponent,
    AllproductComponent,
    AllteamComponent,
    AddteamComponent,
    AddtestimonialsComponent,
    AlltestimonialsComponent,
    AllpromocodeComponent,
    AddpromocodeComponent,
    AllcartitemsComponent,
    
    AllusersComponent
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
    ReactiveFormsModule



  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
