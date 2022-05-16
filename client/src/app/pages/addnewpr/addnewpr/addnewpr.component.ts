import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-addnewpr',
  templateUrl: './addnewpr.component.html',
  styleUrls: ['./addnewpr.component.css']
})
export class AddnewprComponent implements OnInit {
  anewp!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.anewp! = new FormGroup({
      'pname':new FormControl(null, Validators.required),
      'pdesc':new FormControl(null, Validators.required),
      'pimage':new FormControl(null, Validators.required),
      'pvideo':new FormControl(null, Validators.required),
      'gst':new FormControl(null, Validators.required),
      'lprise':new FormControl(null, Validators.required),
      'pdetail':new FormControl(null, Validators.required),
      'psprise':new FormControl(null, Validators.required),
      'hscode':new FormControl(null, Validators.required),
      'status':new FormControl(null, Validators.required),
      'washingi':new FormControl(null, Validators.required),
      'bname':new FormControl(null, Validators.required),
      'pcname':new FormControl(null, Validators.required),
      'pscname':new FormControl(null, Validators.required),
      
    });
  }
  get pname() {
    return this.anewp!.get('pname');
  }
  get pdesc() {
    return this.anewp!.get('pdesc');
  }
  get pimage() {
    return this.anewp!.get('pimage');
  }
  get pvideo() {
    return this.anewp!.get('pvideo');
  }
  get gst() {
    return this.anewp!.get('gst');
  }
  get lprise() {
    return this.anewp!.get('lprise');
  }
  get pdetail() {
    return this.anewp!.get('pdetail');
  }
  get psprise() {
    return this.anewp!.get('psprise');
  }
  get hscode() {
    return this.anewp!.get('hscode');
  }
  get status() {
    return this.anewp!.get('status');
  }
  get washingi() {
    return this.anewp!.get('washingi');
  }
  get bname() {
    return this.anewp!.get('bname');
  }
  get pcname() {
    return this.anewp!.get('pcname');
  }
  get pscname() {
    return this.anewp!.get('pscname');
  }


}
