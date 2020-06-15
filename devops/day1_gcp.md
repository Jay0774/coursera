# Accessing the GCP Console and Cloud Shell

##Overview
In this lab, you become familiar with the GCP web-based interface. Two integrated environments are available:

A GUI environment called the GCP Console
A command-line interface called Cloud Shell, which has the commands from the Cloud SDK pre-installed
In this course, you use both environments.

You need to know a few things about the GCP Console:

The GCP Console is under continuous development, so the graphical layout occasionally changes. Often, these changes are made to accommodate new GCP features or changes in the technology, resulting in a slightly different workflow.

You can perform most common GCP actions in the GCP Console. Sometimes new features are implemented in the Cloud SDK before they are made available in the GCP Console.

The GCP Console is extremely fast for some activities. The GCP Console can perform multiple actions on your behalf that might require many command-line actions.

The commands in the Cloud SDK are valuable tools for automation.

Objectives
In this lab, you learn how to perform the following tasks:

Learn how to access the GCP Console and Cloud Shell

Become familiar with the GCP Console

Become familiar with Cloud Shell features, including the Cloud Shell code editor

Use the GCP Console and Cloud Shell to create buckets and VMs and service accounts

Perform other commands in Cloud Shell

Task 0. Lab Setup
Access Qwiklabs
For each lab, you get a new GCP project and set of resources for a fixed time at no cost.

Make sure you signed into Qwiklabs using an incognito window.

Note the lab's access time (for example, img/time.png and make sure you can finish in that time block.

There is no pause feature. You can restart if needed, but you have to start at the beginning.

When ready, click img/start_lab.png.

Note your lab credentials. You will use them to sign in to Cloud Platform Console. img/open_google_console.png

Click Open Google Console.

Click Use another account and copy/paste credentials for this lab into the prompts.

If you use other credentials, you'll get errors or incur charges.

Accept the terms and skip the recovery resource page.
Do not click End Lab unless you are finished with the lab or want to restart it. This clears your work and removes the project.

After you complete the initial sign-in steps, the project dashboard appears.

GCP Project Dashboard

Task 1. Explore the GCP Console
In this task, you explore the GCP Console and create resources.

Verify that your project is selected
In the Select a project drop-down list in the title bar select the project ID that Qwiklabs provided with your authentication credentials.
The project ID will resemble qwiklabs-gcp- followed by a long hexadecimal number.

Click Cancel to close the dialog.
Your title bar should indicate the project ID as shown in the screenshot. Each lab in the Qwiklabs environment has a unique project ID, as well as unique authentication credentials.

GCP project ID
Navigate to Google Cloud Storage and create a bucket
Cloud Storage allows world-wide storage and retrieval of any amount of data at any time. You can use Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.

Cloud Storage buckets must have a globally unique name. In your organization, you should follow Google Cloud's recommended best practices for naming buckets. For this lab, we can easily get a unique name for our bucket by using the ID of the GCP project that Qwiklabs created for us, because GCP project IDs are also globally unique.

In the GCP Console, on the Navigation menu (Navigation menu), click Home .
In the Dashboard tab of the resulting screen, the Project info section shows your GCP project ID. Select and copy the project ID. Because this project ID was created for you by Qwiklabs, it will resemble qwiklabs-gcp- followed by a long hexadecimal number.
In the GCP Console, on the Navigation menu (Navigationmenu), click Storage > Browser.
Click Create bucket.
For Name, paste in the GCP project ID string you copied in an earlier step. Leave all other values as their defaults.
These lab instructions will later refer to the name that you typed as [BUCKET_NAME].

Click Create.
The GCP Console has a Notifications (notifications icon) icon. Feedback from the underlying commands is sometimes provided there. You can click the icon to check the notifications for additional information and history.

Create a virtual machine (VM) instance
Google Compute Engine offers virtual machines running in Google's datacenters and on its network as a service. Google Kubernetes Engine makes use of Compute Engine as a component of its architecture. For this reason, it's helpful to learn a bit about Compute Engine before learning about Kubernetes Engine.

On the Navigation menu (Navigation menu ), click Compute Engine > VM instances.
Click Create Instance.
For Name, type first-vm as the name for your instance.
For Region, select us-central1.
For Zone, select us-central1-c.
For Machine type, examine the options.
The Machine type: menu lists the number of virtual CPUs, the amount of memory, and a symbolic name such as n1-standard-1. The symbolic name is the parameter you use to select the machine type when using the gcloud command to create a VM. To the right of the region, zone, and machine type is a per-month estimated cost.

To see the breakdown of estimated costs, click Details to the right of the Machine type list underneath the estimated costs.
For Machine type, click 2 vCPUs (n1-standard-2).
How did the cost change?

For Machine type, click f1-micro (1 shared vCPU).
The micro type is a shared-core VM that is inexpensive.

For Firewall, click Allow HTTP traffic.
Leave the remaining settings as their defaults, and click Create.
Wait until the new VM is created.

Explore the VM details
On the VM instances page, click the name of your VM, first-vm.
Locate CPU platform, notice the value, and click Edit.
You can't change the machine type, the CPU platform, or the zone of a running GCP VM. You can add network tags and allow specific network traffic from the internet through firewalls.

Some properties of a VM are integral to the VM and are established when the VM is created. They cannot be changed. Other properties can be edited. For example, you can add disks, and you can determine whether the boot disk is deleted when the instance is deleted.

Scroll down and examine Availability policies.
Compute Engine offers preemptible VM instances, which cost less per hour but can be terminated by GCP at any time. These preemptible instances can save you a lot of money, but you must make sure that your workloads are suitable to be interrupted. You can't convert a non-preemptible instance into a preemptible one. This choice must be made at VM creation.

If a VM is stopped for any reason (for example, an outage or a hardware failure), the automatic restart feature starts it back up. Is this the behavior you want? Are your applications idempotent (written to handle a second startup properly)?

During host maintenance, the VM is set for live migration. However, you can have the VM terminated instead of migrated.

If you make changes, they can sometimes take several minutes to be implemented, especially if they involve networking changes, like adding firewalls or changing the external IP.

Click Cancel.

Create an IAM service account
An IAM service account is a special type of Google account that belongs to an application or a virtual machine, instead of to an individual end user.

On the Navigation menu, click IAM & admin > Service accounts.
Click + Create service account.
On the Service account details page, specify the Service account name as test-service-account.
Click Create.
On the Service account permissions page, specify the role as Project > Editor.
Click Continue.
Click + Create Key.
Select JSON as the key type.
Click Create.
A JSON key file is downloaded. In a later step, you find this key file and upload it to the VM.

Click Close.
Click Done.
Click Check my progress to verify the objective.
Create a bucket, VM instance with necessary firewall rule and an IAM service account.
