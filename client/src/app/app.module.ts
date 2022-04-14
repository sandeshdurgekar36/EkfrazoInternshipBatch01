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
import { MatNativeDateModule} from '@angular/material/core'


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { HomeComponent } from './pages/home/home.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { AddnewprComponent } from './pages/addnewpr/addnewpr/addnewpr.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';

 
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MasterpageComponent,
    HomeComponent,
    NewuserComponent,
    ImportuserComponent,
    AddnewprComponent,
    AllproductComponent
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



  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
