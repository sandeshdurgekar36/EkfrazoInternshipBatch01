import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlaceordComponent } from './placeord.component';

describe('PlaceordComponent', () => {
  let component: PlaceordComponent;
  let fixture: ComponentFixture<PlaceordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlaceordComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlaceordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
