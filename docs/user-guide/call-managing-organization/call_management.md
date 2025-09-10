# Call management

## Overview

Call management in Waldur enables organizations to manage resource allocation through a structured application proposals and review process. This feature is particularly useful for research institutions, funding agencies, and organizations that need to allocate computational or infrastructure resources through a competitive process.

## Introduction

Call management in Waldur is built around structured components: calls, rounds, proposals, and reviews. A call is a defined period during which resources can be allocated. Each call is divided into rounds, where stakeholders can submit and review proposals for resource allocation. Proposals are evaluated through a structured review process. Successful proposals lead to approved allocations, seamlessly integrating into the rest of the Waldur ecosystem. When a proposal is approved, Waldur automatically creates a project under the proposing organization that initiated the call. Allocations are granted to this project, and team members who submitted the proposal are added to the project, ensuring the resources are immediately ready for use.

This guide walks you through the entire lifecycle of call management in Waldur, from setup to final resource allocation. It is structured in a step-by-step format to help each stakeholder understand their responsibilities in the process.

## Stakeholder roles

Different user roles have specific responsibilities within the Call management system:

| Role | Assigned by | Primary responsibilities | Access level |
| --- | --- | --- | --- |
| Organization owner | Staff | <ul><li>Register organization as Call managing organization</li><li>Assign Call organisers</li><li>Oversee overall call management activities</li></ul> | Full access to all calls and organizational data |
| Call organiser | Organization owner | <ul><li>Create calls</li><li>Define call purpose and guidelines</li><li>Assign Call Managers</li><li>Supervise call lifecycle</li></ul> | Access to calls they create and oversee |
| Call manager | Call organiser | <ul><li>Configure call rounds</li><li>Request and manage offerings</li><li>Assign reviewers</li><li>Make allocation decisions</li><li>Monitor call progress</li></ul> | Detailed access to calls they are assigned to |
| Reviewer | Call manager | <ul><li>Evaluate assigned proposals</li><li>Provide scores and feedback</li><li>Recommend approval/rejection</li></ul> | Access limited to assigned proposals |
| Call Member/Applicant | Self-registration | <ul><li>Submit proposals</li><li>Request resources</li></ul> | Access to own proposals and public call information |
| Service Provider | Staff | <ul><li>Provide offerings for calls</li><li>Approve/reject offering requests</li></ul> | Access to offering requests |

## Workflow overview

The call management process follows a sequential workflow:

1. **Preparation**: Organization setup and role assignment (Organization owner → Call organiser → Call manager)
2. **Call setup**: Creation of call framework by Call organiser and detailed configuration by Call Manager
3. **Resource preparation**: Request and confirmation of offerings from service providers
4. **Submission period**: Opening call for proposal submissions
5. **Evaluation**: Review and assessment of submitted proposals
6. **Decision**: Acceptance or rejection of proposals
7. **Allocation**: Automatic provisioning of resources for approved proposals
8. **Monitoring**: Oversight of active allocations and reporting

```mermaid
flowchart TD
    %% Styling
    classDef orgOwner fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#000
    classDef callOrg fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    classDef callMgr fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px,color:#000
    classDef reviewer fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    classDef applicant fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000
    classDef provider fill:#f1f8e9,stroke:#558b2f,stroke-width:2px,color:#000
    classDef system fill:#f5f5f5,stroke:#616161,stroke-width:2px,color:#000
    classDef decision fill:#fff8e1,stroke:#f57f17,stroke-width:2px,color:#000
    
    %% Row 1: Stakeholders (Horizontal)
    subgraph stakeholders["👥 Key Stakeholders"]
        direction LR
        R1["👤 Organization Owner<br/> Organization setup & Role assignment"] --> R2["📋 Call organiser<br/>Create & Oversee calls"] 
        R2 --> R3["⚙️ Call manager<br/>Configure & Manage"]
        R3 --> R4["🔍 Reviewer<br/>Evaluate proposals"]
        R4 --> R5["📝 Applicant<br/>Submit proposals"]
        R5 --> R6["✅ Service provider<br/>Approve resources"]
    end
    
    %% Row 2: Setup to Submission (Horizontal)
    subgraph setup["🏗️ Setup & Submission phase"]
        direction LR
        A[📋 Call organiser<br/>Create Call] --> B[👨‍💼 Assign<br/>Call Manager]
        B --> C[⚙️ Configure Round<br/>& Settings]
        C --> D[📋 Request<br/>Offerings]
        D --> E[✅ Provider<br/>Approve Resources]
        E --> F[🚀 Activate<br/>Call]
        F --> G[📝 Applicants<br/>Submit Proposals]
    end
    
    %% Row 3: Review to Completion (Horizontal)
    subgraph review["🔍 Review & Allocation Phase"]
        direction LR
        H{Review<br/>Assignment} -->|Auto| I[🤖 Auto-assign<br/>Reviews]
        H -->|Manual| J[👨‍💼 Manual<br/>Assignment]
        I --> K[🔍 Reviewers<br/>Evaluate]
        J --> K
        K --> L{Final<br/>Decision}
        L -->|Manager| M[👨‍💼 Accept/<br/>Reject]
        L -->|Auto| N[🤖 Auto-approve<br/>if Score ≥ Threshold]
        M --> O{Approved?}
        N --> O
        O -->|Yes| P[🏗️ Create Project &<br/>Allocate Resources]
        O -->|No| Q[❌ Notify<br/>Rejection]
        P --> S[📊 Monitor &<br/>Report]
        Q --> S
    end
    
    %% Connections between rows
    stakeholders -.-> A
    G --> H
    
    %% Apply styles
    class R1,A orgOwner
    class R2,B callOrg
    class R3,C,F,J,M callMgr
    class R4,K reviewer
    class R5,G applicant
    class R6,E provider
    class I,N,P system
    class H,L,O decision
```

## Detailed process guide

## Step 1: Organization setup  

**Performed by:** Organization owner

1. **Verify organization type**:
      - Navigate to your organization's profile settings
      - Confirm your organization is registered as a **Call managing organization**
      - If not, contact your Waldur administrator to update your organization type

2. **Review available offerings**:
      - Check that there are **marketplace offerings** available to be requested in calls
      - These offerings will form the resource pool available for allocation

3. **Assign Call organisers**:
      - Go to the **Team** section of your organization
      - Click on the **Add member** button
      - Search for users to assign as Call organisers
      - Select the **Call organiser** role from the dropdown menu
      - Click **Add** to confirm the assignment

![Screenshot: Organization Setup for Call management](../img/org_setup_call_management.png)

## Step 2: Call creation

**Performed by:** Call organiser or Organization owner

1. Navigate to the **Call management** section, in the organisation dashboard.
2. Go to the **Calls** section, to click **"Create call"**.
3. Fill in the following details:
      - Call title
      - Description and documentation
      - Submission guidelines
      - Assign call manager to the call

## Step 3: Configure call rounds  

**Performed by:** Call manager

1. Create a **Round** within the call.
2. Configure the round settings:
      - Start and end dates
      - Review strategy: after round closure or after submission
      - Review duration (in days)
      - Minimum number of reviewers
      - Minimum average score for auto-approval (optional)
      - Deciding entity: call manager or automatic
      - Allocation timing: immediate or fixed date
      - Define the mappings between proposal roles and project roles
3. Assign **reviewers** and **proposal managers**.
4. Save and activate the round.

![Screenshot: Round Configuration Interface](../img/round_creation.png)

## Step 4: Call configuration and activation

**Performed by:** Call manager

Before activating a call, the Call manager must configure all necessary settings:

### Call configuration settings

#### 1. General configuration

Configure the basic call parameters:

- **Fixed duration**: Set whether the call has a fixed timeframe (Yes/No)
- **Reviewer identity visible to submitters**: Choose if applicants can see who is reviewing their proposals (Yes/No)
- **Reviews visible to submitters**: Determine if applicants can view the reviews and feedback (Yes/No)

#### 2. Team management

Assign personnel for the call:

- **Add reviewers**: Select users who will evaluate submitted proposals
- **Add managers**: Additional managers for proposal oversight
  
  *Note: The primary Call manager is added by the Call Organiser during call creation*

#### 3. Offerings configuration

Define available resources:

- **Add Offerings**: Select which service provider offerings will be available for this call
- Ensure all required offerings have been approved by service providers

#### 4. Role mapping

Configure project role assignments:

- **Proposal project role mappings**: Map each proposal role to corresponding project roles
- Each proposal role must be mapped to a project role to ensure proper access when projects are created

*Important: The round must be created and configured first. Only after round configuration is complete can the call be fully configured and activated.*

### Call activation process

Once all configurations are complete:

1. **Review all configurations**:
      - Verify general settings are correct
      - Confirm team assignments are complete
      - Check that offerings are properly configured
      - Ensure role mappings are defined

2. **Activate the call**:
      - Click **"Activate call"** to open it for proposal submissions
      - Once activated, the call becomes visible to potential applicants
      - Applicants can now submit proposals during active rounds

![Screenshot: Call Configuration Interface](../img/call_activation.png)


## Step 5: Submit proposal  

**Performed by:** Call member (Applicant)

Applicants follow these steps to request resources through an active call:

1. Navigate to the **active round** under the relevant call.
2. Click **"Submit proposal"**.
3. Fill in the required fields.
4. Select required **offerings and allocations**.
5. Add **team members** (optional).
6. Upload required documentation.
7. Submit the proposal.

![Screenshot: Proposal Submission Form](../img/proposal_submission_form.png)

## Step 6: Review assignment and process  

**Review Assignment:** Call manager or Automatic system

### Review assignment

**Performed by:** Call manager or Automatic system

After proposals are submitted, reviews must be created and assigned to reviewers. This process depends on the call configuration:

### Automatic review creation

If configured for automatic assignment:

   - System automatically creates reviews
   - Reviews are assigned to available reviewers based on workload
   - Reviewers receive immediate notifications

### Manual review creation

If manual assignment is required:

**Performed by:** Call manager

1. Navigate to the **call**
2. Locate the submitted **proposal** in the proposals list
3. Click **Actions** next to the proposal
4. Select **Create review**
5. Assign the review to specific **reviewers**
6. Reviewers receive notifications of their assignments

![Screenshot: Review Assignment Interface](../img/assign_reviewer.png)

**Performed by:** Reviewer

Reviewers evaluate proposals using a structured assessment process:

1. Reviewer is notified of new assigned proposal.
2. Reviewer clicks **"View"** to open a preview modal:
      - Sees brief proposal summary
      - Can choose to **"Start review"** or **"Reject"** (send back)
3. On clicking **"Start review"**, reviewer is taken to the full review form.
4. Provide feedback and scores on:
      - Project title
      - Summary and description
      - Documentation
      - Resource requests
      - Team composition
5. Submit the review.

![Screenshot: Review Form Interface](../img/review_form1.png)
![Screenshot: Review Form Interface](../img/review_form2.png)

## Step 7: Decision and allocation  

**Performed by:** Call manager (if configured) or Automatic system

The final decision process determines which proposals receive resource allocations:

1. Decision entity evaluates reviews.
2. Proposal is **accepted** or **rejected**.
3. If accepted:
      - A **new project** is created under the proposing organization.
      - Requested resources are provisioned.
      - Team members are added to the project.

![Screenshot: Decision Interface](../img/proposal_decision.png)

## Step 8: Monitoring and reporting  

Effective monitoring ensures the call process runs smoothly and provides valuable insights:

**Performed by:** Call manager and Call organiser

- Use dashboard to monitor:
      - Open/closed calls
      - Round statuses
      - Proposal statuses
      - Review progress
      - Offering request statuses

![Screenshot: Monitoring Dashboard](../img/call_monitoring_dashboard.png)

## Additional tips

- Always check round and call status before making edits.
- Assign enough reviewers early to avoid bottlenecks.
- Communicate with applicants when revisions are needed.
- Keep documentation clear and up to date.

## Troubleshooting

Solutions for common issues encountered during the call management process:

| Issue | Possible Cause | Solution |
| --- | --- | --- |
| Unable to create call | Insufficient permissions | Verify user has Call Organiser role |
| Round cannot be activated | Missing required configuration | Check that all mandatory fields are completed |
| Offering request pending | Service provider hasn't responded | Contact provider directly or through system notification |
| Reviewer cannot access proposal | Incorrect assignment | Verify reviewer assignment in call settings |
| Applicant cannot see active call | Call visibility settings | Check call publication status and visibility settings |
| Resource allocation failed | Insufficient provider capacity | Contact service provider to resolve capacity issue |

## FAQ

**Q: What's the difference between a Call Organiser and a Call Manager?**  
A: A Call Organiser is appointed by the Organization Owner to create calls and assign Call Managers. The Call Manager is responsible for the detailed configuration of calls assigned to them including setting up rounds, assigning reviewers, and managing the review process.

**Q: Can a call have multiple rounds running simultaneously?**  
A: No, Waldur supports multiple rounds within a single call, allowing for different resource types or applicant categories to be handled separately, but they cannot be active at the same time.

**Q: What happens if insufficient reviewers complete their evaluations?**  
A: If the minimum number of reviews is not met by the deadline, the Call manager receives a notification and can either extend the review period or reduce the minimum requirement.

**Q: Can applicants edit their proposals after submission?**  
A: By default, proposals cannot be edited after submission. However, if a reviewer or Call manager rejects a proposal with a request for revisions, the applicant can make the requested changes and resubmit.

**Q: Is it possible to transfer allocated resources between approved projects?**  
A: Resource transfer between projects requires administrative approval. Contact your Call manager to request a resource transfer.

**Q: How are applicants notified about proposal decisions?**  
A: Waldur automatically sends email notifications to all team members listed in a proposal when a decision (approval or rejection) is made.

**Q: Can a Call manager override reviewer scores?**  
A: When configured for Call manager decisions, the manager can approve or reject proposals regardless of review scores, though all reviewer feedback remains visible and documented.