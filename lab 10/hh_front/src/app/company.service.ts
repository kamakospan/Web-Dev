import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Company } from './models/company.interface';
import { Vacancy } from './models/vacancy.interface';

@Injectable({
  providedIn: 'root'
})

export class CompanyService {
  private apiUrl = 'api/';
  constructor(private http: HttpClient) {}

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.apiUrl}/companies`);
  }

  getVacancies(companyId: number): Observable<Vacancy[]> {
    const url = `${this.apiUrl}/companies/${companyId}/vacancies`
    return this.http.get<Vacancy[]>(url);

  }
}
