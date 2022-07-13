import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { PlaceordService } from 'src/app/services/placeord.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-placeord',
  templateUrl: './placeord.component.html',
  styleUrls: ['./placeord.component.css']
})
export class PlaceordComponent implements OnInit {
  plco!: FormGroup;

  constructor(private pService: PlaceordService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.plcoform = new FormGroup({
      'user_id':new FormControl(null, Validators.required),
      'pickup_id':new FormControl(null, Validators.required),
      'drop_id_list':new FormControl(null, Validators.required),
      'vehicles_type_id':new FormControl(null, Validators.required),
      'total_estimated_KM':new FormControl(null, Validators.required),
      'total_estimated_AMT':new FormControl(null, Validators.required),
      'ristrict_no_of_drop':new FormControl(null, Validators.required),
    });
  }
  get user_id() {
    return this.plcoform.get('user_id');
  }
  get pickup_id() {
    return this.plcoform.get('pickup_id');
  }
  get drop_id_list() {
    return this.plcoform.get('drop_id_list');
  }
  get vehicles_type_id() {
    return this.plcoform.get('vehicles_type_id');
  }
  get total_estimated_KM() {
    return this.plcoform.get('total_estimated_KM');
  }
  get total_estimated_AMT() {
    return this.plcoform.get('total_estimated_AMT');
  }
  get ristrict_no_of_drop() {
    return this.plcoform.get('ristrict_no_of_drop');
  }

  plcoform = this.fb.group({
    user_id: ['',Validators.required],
    pickup_id: ['',Validators.required],
    drop_id_list: ['',Validators.required],
    vehicles_type_id: ['',Validators.required],
    total_estimated_KM: ['',Validators.required],
    total_estimated_AMT: ['',Validators.required],
    ristrict_no_of_drop: ['',Validators.required],
  })
  placeords(){
    console.log(this.plcoform.value)
    this.pService.placeords(this.plcoform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
