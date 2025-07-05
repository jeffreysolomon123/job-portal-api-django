import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, JobPost, Applicant

@csrf_exempt
def create_company(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(
            name=data['name'],
            location=data['location'],
            description=data['description']
        )
        return JsonResponse({'message': 'Company created', 'id': company.id})


@csrf_exempt
def post_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.get(id=data['company_id'])
            job = JobPost.objects.create(
                company=company,
                title=data['title'],
                description=data['description'],
                salary=data['salary'],
                location=data['location']
            )
            return JsonResponse({'message': 'Job posted', 'id': job.id})
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found'}, status=404)


def list_jobs(request):
    jobs = JobPost.objects.select_related('company').all()
    job_list = [{
        'id': job.id,
        'title': job.title,
        'company': job.company.name,
        'location': job.location,
        'salary': job.salary
    } for job in jobs]
    return JsonResponse(job_list, safe=False)


@csrf_exempt
def apply_to_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            job = JobPost.objects.get(id=data['job_id'])
            applicant = Applicant.objects.create(
                name=data['name'],
                email=data['email'],
                resume_link=data['resume_link'],
                job=job
            )
            return JsonResponse({'message': 'Application submitted', 'id': applicant.id})
        except JobPost.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)


def get_applicants(request, job_id):
    try:
        applicants = Applicant.objects.filter(job__id=job_id)
        applicant_list = [{
            'name': a.name,
            'email': a.email,
            'resume_link': a.resume_link,
            'applied_at': a.applied_at
        } for a in applicants]
        return JsonResponse(applicant_list, safe=False)
    except JobPost.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
