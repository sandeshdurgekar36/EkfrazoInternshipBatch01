import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { SubsriptionService } from 'src/app/services/subsription.service';
import { Router } from '@angular/router'; 

@Component({
  selector: 'app-subscription',
  templateUrl: './subscription.component.html',
  styleUrls: ['./subscription.component.css']
})
export class SubscriptionComponent implements OnInit {
  

  constructor(private sservice: SubsriptionService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.Subsriptionform = new FormGroup({
      'sub_plan_name':new FormControl(null, Validators.required),
      'validity_period':new FormControl(null, Validators.required),
      'price':new FormControl(null, Validators.required),
            
    });
  }
  get sub_plan_name() {
    return this.Subsriptionform.get('sub_plan_name');
  }
  get price() {
    return this.Subsriptionform.get('price');
  }
  get validity_period() {
    return this.Subsriptionform.get('validity_period');
  }
  Subsriptionform = this.fb.group({
    sub_plan_name :['',Validators.required],
    price :['',Validators.required],
    validity_period :['',Validators.required]
  })
  subsriptions(){
    console.log(this.Subsriptionform.value)
    this.sservice.subsriptions(this.Subsriptionform.value).subscribe(response =>{
      alert("subsription Added")
    },err=>{
      alert("Invalid information")
    })

  }
 


}
