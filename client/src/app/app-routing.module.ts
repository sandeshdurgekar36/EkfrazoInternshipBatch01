import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddnewprComponent } from './pages/addnewpr/addnewpr/addnewpr.component';
import { AllproductComponent } from './pages/allproduct/allproduct/allproduct.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { MasterpageComponent } from './pages/masterpage/masterpage.component';
import { ImportuserComponent } from './pages/newuser/importuser/importuser.component';
import { NewuserComponent } from './pages/newuser/newuser/newuser.component';

const routes: Routes = [
  {path:'',component:HomeComponent},
  {path:'login',component:LoginComponent},
  {path:'masterpage',component:MasterpageComponent},
  {path:'newuser',component:NewuserComponent},
  {path:'importuser',component:ImportuserComponent},
  {path:'addnewpr',component:AddnewprComponent},
  {path:'allproduct',component:AllproductComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
